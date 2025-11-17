import os
import re
import json
import time
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail
from dotenv import load_dotenv
from functools import wraps

app = Flask(__name__)

from model import db, History, Product, Tutorial, User, Cart, Purchase, OTP
from otp import generate_otp, send_otp_email, store_otp_in_db, verify_otp_from_db

# ----------------------------------------------------------------------
# Load environment variables from .env
# ----------------------------------------------------------------------
load_dotenv()

# ----------------------------------------------------------------------
# Flask Secret Key for Sessions
# ----------------------------------------------------------------------
app.secret_key = os.getenv('SECRET_KEY', 'your_secret_key_here')

# ----------------------------------------------------------------------
# SQLAlchemy Database Configuration
# ----------------------------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://rose:makeuptutorial@127.0.0.1/makeup_tutorial'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'
PASSWORD_REGEX = r'^(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$'

with app.app_context():
    db.create_all()

# ----------------------------------------------------------------------
# Payment Functions
# ----------------------------------------------------------------------
def initiate_gcash_payment(amount, order_id, description):
    gcash_app_id = os.getenv('GCASH_APP_ID')
    gcash_app_secret = os.getenv('GCASH_APP_SECRET')

    if not gcash_app_id or not gcash_app_secret:
        return {'status': 'error', 'message': 'GCash credentials not configured'}

    # In a real implementation, you would:
    # 1. Authenticate with GCash API using app_id and app_secret
    # 2. Create a payment intent with the amount, order_id, and description
    # 3. Get the payment URL from GCash response

    # For simulation purposes, create a realistic GCash payment URL
    payment_url = f"https://gcash.com/payment?amount={amount}&order_id={order_id}&description={description}&app_id={gcash_app_id}"

    return {
        'status': 'success',
        'payment_id': f'gcash_{order_id}_{int(time.time())}',
        'redirect_url': payment_url
    }

def initiate_paymaya_payment(amount, order_id, description):
    paymaya_public_key = os.getenv('PAYMAYA_PUBLIC_KEY')
    paymaya_secret_key = os.getenv('PAYMAYA_SECRET_KEY')

    if not paymaya_public_key or not paymaya_secret_key:
        return {'status': 'error', 'message': 'PayMaya credentials not configured'}

    # In a real implementation, you would:
    # 1. Use PayMaya Checkout API to create a payment request
    # 2. Include public_key for authentication
    # 3. Get the checkout URL from PayMaya response

    # For simulation purposes, create a realistic PayMaya payment URL
    payment_url = f"https://paymaya.com/checkout?amount={amount}&order_id={order_id}&description={description}&public_key={paymaya_public_key}"

    return {
        'status': 'success',
        'payment_id': f'paymaya_{order_id}_{int(time.time())}',
        'redirect_url': payment_url
    }

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in first.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in first.', 'warning')
            return redirect(url_for('login'))
        user = User.query.get(session['user_id'])
        if not user or not user.is_admin:
            flash('Admin access required.', 'danger')
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function

@app.context_processor
def inject_current_user():
    if 'user_id' in session:
        return {'current_user': User.query.get(session['user_id'])}
    return {'current_user': None}

@app.route('/')
def index():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user and user.is_admin:
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('home'))
    return render_template('index.html')

# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        flash('You are already logged in.', 'info')
        return redirect(url_for('home'))

    if request.method == 'POST':
        name = request.form.get('name', '').strip().lower()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        # Validate email
        if not re.match(EMAIL_REGEX, email):
            flash('Invalid email address format.', 'danger')
            return redirect(url_for('register'))

        # Validate password
        if not re.match(PASSWORD_REGEX, password):
            flash('Password must be at least 8 characters long and contain a special character.', 'danger')
            return redirect(url_for('register'))

        # Check for existing user
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already in use.', 'warning')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').strip().lower()
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['email'] = user.email
            session['name'] = user.name
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

# ---------------- HOME ----------------
@app.route('/home')
@login_required
def home():
    return render_template('home.html', name=session.get('name'))

# ---------------- TUTORIAL ----------------
@app.route('/tutorial')
@login_required
def tutorial():
    category = request.args.get('category', 'All')
    if category == 'All':
        tutorials = Tutorial.query.all()
    else:
        tutorials = Tutorial.query.filter_by(category=category).all()
    categories = ['All', 'Glam Look', 'No Makeup Look', 'Latina Makeup']
    return render_template('tutorial.html', tutorials=tutorials, categories=categories, selected_category=category)

@app.route('/tutorial/<int:tutorial_id>')
@login_required
def tutorial_detail(tutorial_id):
    tutorial = Tutorial.query.get_or_404(tutorial_id)
    # Track history
    history = History(user_id=session['user_id'], action=f"Viewed tutorial: {tutorial.title}", tutorial_type="Tutorial")
    db.session.add(history)
    db.session.commit()
    steps = json.loads(tutorial.steps) if tutorial.steps.startswith('[') else tutorial.steps.split(',')
    return render_template('tutorial_detail.html', tutorial=tutorial, steps=steps)

# ---------------- SHOP ----------------
@app.route('/shop')
@login_required
def shop():
    products = Product.query.all()
    cart_count = Cart.query.filter_by(user_id=session['user_id']).count()
    return render_template('shop.html', products=products, cart_count=cart_count)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    quantity = int(request.form.get('quantity', 1))

    # Check if item already in cart
    existing_cart_item = Cart.query.filter_by(user_id=session['user_id'], product_id=product_id).first()
    if existing_cart_item:
        existing_cart_item.quantity += quantity
    else:
        cart_item = Cart(user_id=session['user_id'], product_id=product_id, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()
    flash(f'Added {quantity} x {product.name} to cart!', 'success')
    return redirect(url_for('shop'))

@app.route('/cart')
@login_required
def cart():
    cart_items = Cart.query.filter_by(user_id=session['user_id']).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/remove_from_cart/<int:cart_id>', methods=['POST'])
@login_required
def remove_from_cart(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)
    if cart_item.user_id != session['user_id']:
        flash('Unauthorized action.', 'danger')
        return redirect(url_for('cart'))

    db.session.delete(cart_item)
    db.session.commit()
    flash('Item removed from cart.', 'success')
    return redirect(url_for('cart'))

# ---------------- CHECKOUT & PAYMENT ----------------
@app.route('/checkout', methods=['POST'])
@login_required
def checkout():
    selected_item_ids = request.form.getlist('selected_items')
    name = request.form.get('name')
    address = request.form.get('address')
    contact = request.form.get('contact')

    if not selected_item_ids:
        flash('Please select items to checkout.', 'warning')
        return redirect(url_for('cart'))

    # Get selected cart items
    cart_items = Cart.query.filter(
        Cart.id.in_(selected_item_ids), 
        Cart.user_id == session['user_id']
    ).all()

    if not cart_items:
        flash('No valid items selected.', 'warning')
        return redirect(url_for('cart'))

    # Calculate totals
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    discount = subtotal * 0.10  # 10% discount
    total = subtotal - discount

    # Generate order ID
    order_id = f"ORD-{int(time.time())}"

    # Store order data in session
    session[f'order_{order_id}'] = {
        'selected_item_ids': selected_item_ids,
        'cart_items': [
            {
                'product_name': item.product.name,
                'quantity': item.quantity,
                'price': item.product.price,
                'subtotal': item.product.price * item.quantity
            }
            for item in cart_items
        ],
        'subtotal': subtotal,
        'discount': discount,
        'total': total,
        'shipping_info': {
            'name': name,
            'address': address,
            'contact': contact
        }
    }

    return redirect(url_for('payment', order_id=order_id))

@app.route('/payment/<order_id>', methods=['GET', 'POST'])
@login_required
def payment(order_id):
    # Retrieve order data from session or database
    order_data = session.get(f'order_{order_id}')
    if not order_data:
        flash('Order not found or expired.', 'danger')
        return redirect(url_for('cart'))
    
    if request.method == 'POST':
        payment_method = request.form.get('payment_method')
        
        if payment_method == 'GCash':
            # Process GCash payment
            payment_response = initiate_gcash_payment(
                amount=order_data['total'],
                order_id=order_id,
                description=f"Order {order_id}"
            )
            if payment_response['status'] == 'success':
                # Store payment info in session
                session[f'payment_{order_id}'] = {
                    'payment_id': payment_response['payment_id'],
                    'method': 'GCash',
                    'status': 'pending'
                }
                return redirect(payment_response['redirect_url'])
            else:
                flash('Failed to initiate GCash payment.', 'danger')
                return redirect(url_for('payment', order_id=order_id))
                
        elif payment_method == 'PayMaya':
            # Process PayMaya payment
            payment_response = initiate_paymaya_payment(
                amount=order_data['total'],
                order_id=order_id,
                description=f"Order {order_id}"
            )
