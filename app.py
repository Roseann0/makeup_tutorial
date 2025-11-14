import os
import re
import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from functools import wraps

from model import db, History, Product, Tutorial, User, Cart, Purchase

# ----------------------------------------------------------------------
# Load environment variables from .env
# ----------------------------------------------------------------------
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev_secret_key')

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

@app.route('/checkout', methods=['POST'])
@login_required
def checkout():
    selected_item_ids = request.form.getlist('selected_items')
    payment_method = request.form.get('payment_method', 'Cash on Delivery')
    name = request.form.get('name')
    address = request.form.get('address')
    contact = request.form.get('contact')

    if not selected_item_ids:
        return redirect(url_for('cart'))

    # Get selected cart items
    cart_items = Cart.query.filter(Cart.id.in_(selected_item_ids), Cart.user_id == session['user_id']).all()

    if not cart_items:
        return redirect(url_for('cart'))

    # Calculate totals
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    discount = subtotal * 0.10  # 10% discount
    total = subtotal - discount

    # Generate order ID (using timestamp for simplicity)
    import time
    order_id = f"ORD-{int(time.time())}"

    # Create purchases and clear cart
    for item in cart_items:
        purchase = Purchase(
            user_id=session['user_id'],
            product_id=item.product_id,
            quantity=item.quantity,
            total_price=item.product.price * item.quantity,
            payment_method=payment_method
        )
        db.session.add(purchase)

        # Track history
        history = History(
            user_id=session['user_id'],
            action=f"Purchased: {item.product.name} (x{item.quantity})",
            tutorial_type="Purchase"
        )
        db.session.add(history)

        # Remove from cart
        db.session.delete(item)

    db.session.commit()

    # Store order data in session for summary page
    session['order_data'] = {
        'name': name,
        'email': session.get('email'),
        'address': address,
        'contact': contact,
        'payment_method': payment_method,
        'selected_items': [{'id': item.id, 'product': {'name': item.product.name, 'description': item.product.description, 'price': item.product.price}, 'quantity': item.quantity} for item in cart_items],
        'subtotal': subtotal,
        'discount': discount,
        'total': total,
        'order_id': order_id,
        'order_date': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    }

    return redirect(url_for('order_summary'))

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

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = User.query.get(session['user_id'])
    history = History.query.filter_by(user_id=session['user_id']).order_by(History.created_at.desc()).all()
    purchases = Purchase.query.filter_by(user_id=session['user_id']).order_by(Purchase.created_at.desc()).all()

    if request.method == 'POST':
        name = request.form.get('name', '').strip().lower()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        # Validate email
        if not re.match(EMAIL_REGEX, email):
            flash('Invalid email address format.', 'danger')
            return redirect(url_for('profile'))

        # Check if email is already taken by another user
        existing_user = User.query.filter_by(email=email).first()
        if existing_user and existing_user.id != user.id:
            flash('Email already in use.', 'warning')
            return redirect(url_for('profile'))

        # Update user info
        user.name = name
        user.email = email
        if password:
            if not re.match(PASSWORD_REGEX, password):
                flash('Password must be at least 8 characters long and contain a special character.', 'danger')
                return redirect(url_for('profile'))
            user.password_hash = generate_password_hash(password)

        db.session.commit()
        session['email'] = email
        session['name'] = name
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))

    return render_template('profile.html', user=user, history=history, purchases=purchases)

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

# ---------------- ADMIN DASHBOARD ----------------
@app.route('/admin')
@admin_required
def admin():
    users = User.query.order_by(User.created_at.desc()).all()
    products = Product.query.all()
    tutorials = Tutorial.query.all()
    purchases = Purchase.query.order_by(Purchase.created_at.desc()).all()
    histories = History.query.order_by(History.created_at.desc()).limit(50).all()
    return render_template('admin.html', users=users, products=products, tutorials=tutorials, purchases=purchases, histories=histories)

@app.route('/admin/users')
@admin_required
def admin_users():
    users = User.query.order_by(User.created_at.desc()).all()
    return render_template('admin_users.html', users=users)

@app.route('/admin/users/<int:user_id>/toggle', methods=['POST'])
@admin_required
def toggle_admin(user_id):
    user = User.query.get_or_404(user_id)
    user.is_admin = not user.is_admin
    db.session.commit()
    flash(f"User {user.name} {'promoted to' if user.is_admin else 'demoted from'} admin.", 'success')
    return redirect(url_for('admin_users'))

@app.route('/admin/products')
@admin_required
def admin_products():
    products = Product.query.all()
    return render_template('admin_products.html', products=products)

@app.route('/admin/products/add', methods=['POST'])
@admin_required
def add_product():
    name = request.form.get('name')
    description = request.form.get('description')
    price = float(request.form.get('price'))
    category = request.form.get('category')
    image_url = request.form.get('image_url') or None

    product = Product(name=name, description=description, price=price, category=category, image_url=image_url)
    db.session.add(product)
    db.session.commit()
    flash('Product added successfully!', 'success')
    return redirect(url_for('admin_products'))

@app.route('/admin/products/edit', methods=['POST'])
@admin_required
def edit_product():
    product_id = request.form.get('product_id')
    product = Product.query.get_or_404(product_id)

    product.name = request.form.get('name')
    product.description = request.form.get('description')
    product.price = float(request.form.get('price'))
    product.category = request.form.get('category')
    product.image_url = request.form.get('image_url') or None

    db.session.commit()
    flash('Product updated successfully!', 'success')
    return redirect(url_for('admin_products'))

@app.route('/admin/products/<int:product_id>/delete', methods=['POST'])
@admin_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('admin_products'))

@app.route('/admin/tutorials')
@admin_required
def admin_tutorials():
    tutorials = Tutorial.query.all()
    return render_template('admin_tutorials.html', tutorials=tutorials)

@app.route('/admin/tutorials/add', methods=['POST'])
@admin_required
def add_tutorial():
    title = request.form.get('title')
    description = request.form.get('description')
    category = request.form.get('category')
    difficulty = request.form.get('difficulty')
    duration = int(request.form.get('duration'))
    steps = request.form.get('steps')

    tutorial = Tutorial(
        title=title,
        description=description,
        category=category,
        difficulty=difficulty,
        duration=duration,
        steps=steps,
        user_id=session['user_id']
    )
    db.session.add(tutorial)
    db.session.commit()
    flash('Tutorial added successfully!', 'success')
    return redirect(url_for('admin_tutorials'))

@app.route('/admin/tutorials/edit', methods=['POST'])
@admin_required
def edit_tutorial():
    tutorial_id = request.form.get('tutorial_id')
    tutorial = Tutorial.query.get_or_404(tutorial_id)

    tutorial.title = request.form.get('title')
    tutorial.description = request.form.get('description')
    tutorial.category = request.form.get('category')
    tutorial.difficulty = request.form.get('difficulty')
    tutorial.duration = int(request.form.get('duration'))
    tutorial.steps = request.form.get('steps')

    db.session.commit()
    flash('Tutorial updated successfully!', 'success')
    return redirect(url_for('admin_tutorials'))

@app.route('/admin/tutorials/<int:tutorial_id>/delete', methods=['POST'])
@admin_required
def delete_tutorial(tutorial_id):
    tutorial = Tutorial.query.get_or_404(tutorial_id)
    db.session.delete(tutorial)
    db.session.commit()
    flash('Tutorial deleted successfully!', 'success')
    return redirect(url_for('admin_tutorials'))

@app.route('/delete_history/<int:history_id>', methods=['POST'])
@login_required
def delete_history(history_id):
    history = History.query.get_or_404(history_id)
    if history.user_id != session['user_id']:
        flash('Unauthorized action.', 'danger')
        return redirect(url_for('profile'))
    db.session.delete(history)
    db.session.commit()
    flash('Activity deleted.', 'success')
    return redirect(url_for('profile'))

@app.route('/rate_purchase/<int:purchase_id>', methods=['POST'])
@login_required
def rate_purchase(purchase_id):
    purchase = Purchase.query.get_or_404(purchase_id)
    if purchase.user_id != session['user_id']:
        flash('Unauthorized action.', 'danger')
        return redirect(url_for('profile'))

    rating = request.form.get('rating', type=int)
    received = request.form.get('received') == 'on'

    if rating is not None and 0 <= rating <= 5:
        purchase.rating = rating
    purchase.received = received

    db.session.commit()
    flash('Purchase updated successfully!', 'success')
    return redirect(url_for('profile'))

@app.route('/order_summary')
@login_required
def order_summary():
    order_data = session.get('order_data')
    if not order_data:
        flash('No order data found.', 'warning')
        return redirect(url_for('cart'))

    # Clear the order data from session after displaying
    session.pop('order_data', None)

    return render_template('order_summary.html', **order_data)

# ----------------------------------------------------------------------
# Run the Flask app
# ----------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
