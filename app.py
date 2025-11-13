import os
import re
import json
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from functools import wraps
from model import db, User, Tutorial, Product, History, Purchase, Cart  # make sure your file is named model.py

# ----------------------------------------------------------------------
# Load environment variables from .env
# ----------------------------------------------------------------------
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev_secret_key')

# ----------------------------------------------------------------------
# MySQL Database Configuration (for XAMPP or other MySQL server)
# ----------------------------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

# ----------------------------------------------------------------------
# Validation Regex
# ----------------------------------------------------------------------
EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'
PASSWORD_REGEX = r'^(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$'

# ----------------------------------------------------------------------
# Create tables (for Flask 3.0+)
# ----------------------------------------------------------------------
with app.app_context():
    db.create_all()

# ----------------------------------------------------------------------
# Login Required Decorator
# ----------------------------------------------------------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in first.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# ----------------------------------------------------------------------
# Routes
# ----------------------------------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    # If already logged in
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
            flash('Email already registered. Try logging in.', 'warning')
            return redirect(url_for('login'))

        # Hash password and save user
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
    # If already logged in
    if 'user_id' in session:
        flash('You are already logged in.', 'info')
        return redirect(url_for('home'))

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
    categories = ['All'] + [cat[0] for cat in db.session.query(Tutorial.category).distinct().all()]
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

@app.route('/checkout', methods=['POST'])
@login_required
def checkout():
    cart_items = Cart.query.filter_by(user_id=session['user_id']).all()
    if not cart_items:
        flash('Your cart is empty.', 'warning')
        return redirect(url_for('cart'))

    # Process purchases
    for item in cart_items:
        total_price = item.product.price * item.quantity
        purchase = Purchase(user_id=session['user_id'], product_id=item.product_id, quantity=item.quantity, total_price=total_price)
        db.session.add(purchase)
        # Track history
        history = History(user_id=session['user_id'], action=f"Purchased: {item.product.name} (x{item.quantity})", tutorial_type="Purchase")
        db.session.add(history)

    # Clear cart
    Cart.query.filter_by(user_id=session['user_id']).delete()
    db.session.commit()

    flash('Checkout successful! Your purchases have been processed.', 'success')
    return redirect(url_for('profile'))

@app.route('/buy/<int:product_id>', methods=['POST'])
@login_required
def buy_product(product_id):
    product = Product.query.get_or_404(product_id)
    quantity = int(request.form.get('quantity', 1))
    total_price = product.price * quantity
    purchase = Purchase(user_id=session['user_id'], product_id=product_id, quantity=quantity, total_price=total_price)
    db.session.add(purchase)
    # Track history
    history = History(user_id=session['user_id'], action=f"Purchased: {product.name} (x{quantity})", tutorial_type="Purchase")
    db.session.add(history)
    db.session.commit()
    flash(f'Purchase successful! You bought {quantity} x {product.name}.', 'success')
    return redirect(url_for('shop'))

# ---------------- PROFILE ----------------
@app.route('/profile')
@login_required
def profile():
    user = User.query.get(session['user_id'])
    history = History.query.filter_by(user_id=session['user_id']).order_by(History.created_at.desc()).all()
    purchases = Purchase.query.filter_by(user_id=session['user_id']).order_by(Purchase.created_at.desc()).all()
    return render_template('profile.html', user=user, history=history, purchases=purchases)

# ---------------- DESCRIPTION ----------------
@app.route('/description')
@login_required
def description():
    products = Product.query.all()  # For product descriptions
    suggestions = {
        'tones': ['Fair', 'Medium', 'Tan', 'Deep'],
        'tips': [
            'Dry skin: Use hydrating primer and cream foundation.',
            'Oily skin: Try mattifying primer and oil-control powder.',
            'Warm undertone: Choose peach/golden shades.',
            'Cool undertone: Choose pink/rosy shades.'
        ]
    }
    return render_template('description.html', suggestions=suggestions, products=products)

# ---------------- LOGOUT ----------------
@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash('You have logged out.', 'info')
    return redirect(url_for('login'))

# ----------------------------------------------------------------------
# Run the Flask app
# ----------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
