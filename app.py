import os
import re
import json
import time
import random
import string
from datetime import datetime, timedelta

from flask import (
    Flask, render_template, request, redirect, url_for,
    flash, session, jsonify
)
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from functools import wraps
from flask_mail import Mail, Message
from flask_wtf.csrf import CSRFProtect

# MODELS
from model import db, History, Product, Tutorial, User, Cart, Purchase

# -------------------------------------------------------
# FLASK APP INIT
# -------------------------------------------------------
app = Flask(__name__)

# LOAD .env
load_dotenv()

# SECRET KEY
app.secret_key = os.getenv("SECRET_KEY", "mysecretkey")
csrf = CSRFProtect(app)

# -------------------------------------------------------
# SQLALCHEMY CONFIG (FIXED)
# -------------------------------------------------------
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_NAME = os.getenv("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# -------------------------------------------------------
# MAIL CONFIG (FIXED)
# -------------------------------------------------------
app.config['MAIL_SERVER'] = os.getenv("MAIL_SERVER", "smtp.gmail.com")
app.config['MAIL_PORT'] = int(os.getenv("MAIL_PORT", 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("MAIL_DEFAULT_SENDER")

mail = Mail(app)

# -------------------------------------------------------
# CSRF PROTECTION
# -------------------------------------------------------
csrf = CSRFProtect(app)

# -------------------------------------------------------
# CONSTANTS & REGEX
# -------------------------------------------------------
EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'
PASSWORD_REGEX = r'^(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$'
# Philippine mobile number regex (11 digits starting with 09)
PH_MOBILE_REGEX = r'^09\d{9}$'

# -------------------------------------------------------
# DATABASE INITIALIZATION
# -------------------------------------------------------
with app.app_context():
    db.create_all()

# -------------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------------
def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

def send_otp_email(email, otp):
    """Send OTP to email"""
    try:
        msg = Message("Your OTP Code", recipients=[email])
        msg.body = f"Your OTP is: {otp}. It expires in 10 minutes."
        mail.send(msg)
        return True
    except Exception as e:
        print("Email sending error:", e)
        return False

def validate_ph_mobile_number(number):
    """Validate Philippine mobile number"""
    if not number:
        return False
    # Remove any spaces, dashes, or other characters
    cleaned_number = re.sub(r'[\s\-\(\)\+]', '', number)
    # Check if it matches the Philippine mobile number format
    return bool(re.match(PH_MOBILE_REGEX, cleaned_number))

# -------------------------------------------------------
# LOGIN REQUIRED DECORATOR
# -------------------------------------------------------
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in first.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper

# -------------------------------------------------------
# ADMIN REQUIRED DECORATOR
# -------------------------------------------------------
def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        user = User.query.get(session["user_id"])
        if not user or not user.is_admin:
            flash("Admin access required.", "danger")
            return redirect(url_for("home"))
        return f(*args, **kwargs)
    return wrapper

# -------------------------------------------------------
# AUTO-INJECT USER INTO ALL TEMPLATES
# -------------------------------------------------------
@app.context_processor
def inject_current_user():
    user = None
    if "user_id" in session:
        user = User.query.get(session["user_id"])
    return {"current_user": user}

# -------------------------------------------------------
# HOME PAGE
# -------------------------------------------------------
@app.route("/")
def index():
    if "user_id" in session:
        user = User.query.get(session["user_id"])
        if user and user.is_admin:
            return redirect(url_for("admin"))
        return redirect(url_for("home"))
    return render_template("index.html")

@app.route("/tutorial")
@login_required
def tutorial():
    # Read selected category from query string
    selected_category = request.args.get("category", "All")

    # Get distinct categories from tutorials
    categories = [cat[0] for cat in db.session.query(Tutorial.category).distinct()]

    # Add an "All" option
    categories.insert(0, "All")

    # Filter tutorials if a category is selected
    if selected_category != "All":
        tutorials = Tutorial.query.filter_by(category=selected_category).all()
    else:
        tutorials = Tutorial.query.all()

    return render_template(
        "tutorial.html",
        tutorials=tutorials,
        categories=categories,
        selected_category=selected_category
    )

@app.route("/description")
@login_required
def description():
    # Data for the suggestions section
    suggestions = {
        "tones": [
            "Fair",
            "Light",
            "Medium",
            "Tan",
            "Olive",
            "Deep"
        ],
        "tips": [
            "Match your foundation to your neck.",
            "Choose warm undertones for golden skin.",
            "Cool tones look great with rosy undertones.",
            "Always prep your skin with moisturizer.",
            "Blend your makeup thoroughly for a natural look."
        ]
    }

    # Example product list (you can replace this with DB query)
    products = [
        {
            "name": "Matte Foundation",
            "description": "Perfect for oily or combination skin.",
            "price": 599.00,
            "category": "Foundation"
        },
        {
            "name": "Hydrating Concealer",
            "description": "Gives a natural brightened finish.",
            "price": 349.00,
            "category": "Concealer"
        },
    ]

    return render_template(
        "description.html",
        suggestions=suggestions,
        products=products
    )

# -------------------------------------------------------
# REGISTER
# -------------------------------------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if "user_id" in session:
        flash("You are already logged in.", "info")
        return redirect(url_for("home"))

    if request.method == "POST":
        name = request.form.get("name", "").strip().lower()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password")

        # Validate email
        if not re.match(EMAIL_REGEX, email):
            flash("Invalid email format.", "danger")
            return redirect(url_for("register"))

        # Validate password
        if not re.match(PASSWORD_REGEX, password):
            flash("Password must be 8+ chars with 1 special character.", "danger")
            return redirect(url_for("register"))

        # Check existing email
        if User.query.filter_by(email=email).first():
            flash("Email already registered.", "warning")
            return redirect(url_for("register"))

        # Generate OTP
        otp = generate_otp()

        # Save pending registration
        session["pending_registration"] = {
            "name": name,
            "email": email,
            "password_hash": generate_password_hash(password),
            "otp": otp,
            "expires_at": (datetime.utcnow() + timedelta(minutes=10)).timestamp()
        }

        # Send email
        if send_otp_email(email, otp):
            flash("OTP sent to your email.", "info")
            return redirect(url_for("verify_otp"))

        flash("Failed to send OTP.", "danger")
        return redirect(url_for("register"))

    return render_template("register.html")

@app.route("/verify_otp", methods=["GET", "POST"])
def verify_otp():
    if "pending_registration" not in session:
        flash("No pending registration.", "warning")
        return redirect(url_for("register"))

    data = session["pending_registration"]

    if datetime.utcnow().timestamp() > data["expires_at"]:
        session.pop("pending_registration", None)
        flash("OTP expired. Try again.", "danger")
        return redirect(url_for("register"))

    if request.method == "POST":
        otp_code = request.form.get("otp")
        if otp_code == data["otp"]:
            new_user = User(
                name=data["name"],
                email=data["email"],
                password_hash=data["password_hash"]
            )
            db.session.add(new_user)
            db.session.commit()

            session.pop("pending_registration", None)

            flash("Account created!", "success")
            return redirect(url_for("login"))

        flash("Invalid OTP.", "danger")
        return redirect(url_for("verify_otp"))

    return render_template("verify_otp.html")

# -------------------------------------------------------
# LOGIN
# -------------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            otp = generate_otp()
            session["login_otp"] = {
                "otp": otp,
                "email": user.email,
                "user_id": user.id,
                "name": user.name,
                "expires_at": (datetime.utcnow() + timedelta(minutes=10)).timestamp()
            }

            if send_otp_email(email, otp):
                flash("OTP sent to your email.", "info")
                return redirect(url_for("verify_login_otp"))

            flash("Failed to send OTP.", "danger")
            return redirect(url_for("login"))

        flash("Invalid credentials.", "danger")
        return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/verify_login_otp", methods=["GET", "POST"])
def verify_login_otp():
    if "login_otp" not in session:
        flash("No pending login.", "warning")
        return redirect(url_for("login"))

    data = session["login_otp"]

    if datetime.utcnow().timestamp() > data["expires_at"]:
        session.pop("login_otp", None)
        flash("OTP expired.", "danger")
        return redirect(url_for("login"))

    if request.method == "POST":
        otp_code = request.form.get("otp")

        if otp_code == data["otp"]:
            session["user_id"] = data["user_id"]
            session["email"] = data["email"]
            session["name"] = data["name"]

            session.pop("login_otp", None)

            flash("Login successful!", "success")
            return redirect(url_for("home"))

        flash("Invalid OTP.", "danger")
        return redirect(url_for("verify_login_otp"))

    return render_template("verify_login_otp.html")

# -------------------------------------------------------
# LOGOUT
# -------------------------------------------------------
@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for("index"))

# -------------------------------------------------------
# HOME
# -------------------------------------------------------
@app.route("/home")
@login_required
def home():
    tutorials = Tutorial.query.all()
    return render_template("home.html", tutorials=tutorials)

# -------------------------------------------------------
# TUTORIALS
# -------------------------------------------------------
@app.route("/tutorial/<int:tutorial_id>")
@login_required
def tutorial_detail(tutorial_id):
    tutorial = Tutorial.query.get_or_404(tutorial_id)

    history = History(
        user_id=session["user_id"],
        action=f"Viewed tutorial: {tutorial.title}",
        tutorial_type="Tutorial"
    )
    db.session.add(history)
    db.session.commit()

    return render_template("tutorial_detail.html", tutorial=tutorial)

@app.route("/tutorial/step/category/<category>")
@login_required
def tutorial_step_category(category):
    tutorials = Tutorial.query.filter_by(category=category).all()
    return render_template(
        "tutorial_step_category.html",
        tutorials=tutorials,
        category=category
    )

@app.route(
    "/tutorial/video/<int:tutorial_id>",
    endpoint="tutorial_video"
)
@login_required
def tutorial_video(tutorial_id):
    tutorial = Tutorial.query.get_or_404(tutorial_id)
    return render_template("tutorial_video.html", tutorial=tutorial)

@app.route(
    "/tutorial/video/category/<category>",
    endpoint="tutorial_video_category"
)
@login_required
def tutorial_video_category(category):
    tutorials = Tutorial.query.filter_by(category=category).all()
    return render_template(
        "tutorial_video_category.html",
        tutorials=tutorials,
        category=category
    )

# -------------------------------------------------------
# SHOP & CART
# -------------------------------------------------------
@app.route("/shop")
@login_required
def shop():
    products = Product.query.all()
    cart_count = Cart.query.filter_by(user_id=session["user_id"]).count()
    return render_template("shop.html", products=products, cart_count=cart_count)

@app.route("/add_to_cart/<int:product_id>", methods=["POST"])
@login_required
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    quantity = int(request.form.get("quantity", 1))

    existing = Cart.query.filter_by(
        user_id=session["user_id"],
        product_id=product_id
    ).first()

    if existing:
        existing.quantity += quantity
    else:
        db.session.add(Cart(user_id=session["user_id"], product_id=product_id, quantity=quantity))

    db.session.commit()
    flash(f"Added {quantity} × {product.name} to cart!", "success")
    return redirect(url_for("shop"))

@app.route("/cart")
@login_required
def cart():
    cart_items = Cart.query.filter_by(user_id=session["user_id"]).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template("cart.html", cart_items=cart_items, total=total)

@app.route("/remove_from_cart/<int:cart_id>", methods=["POST"])
@login_required
def remove_from_cart(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)

    if cart_item.user_id != session["user_id"]:
        flash("Unauthorized.", "danger")
        return redirect(url_for("cart"))

    db.session.delete(cart_item)
    db.session.commit()

    flash("Item removed.", "success")
    return redirect(url_for("cart"))

@app.route("/update_cart_quantity/<int:cart_id>", methods=["POST"])
@login_required
def update_cart_quantity(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)

    if cart_item.user_id != session["user_id"]:
        return jsonify({"success": False}), 403

    data = request.get_json()
    quantity = data.get("quantity", 1)

    if not isinstance(quantity, int) or quantity < 1 or quantity > 99:
        return jsonify({"success": False}), 400

    cart_item.quantity = quantity
    db.session.commit()
    return jsonify({"success": True})

# -------------------------------------------------------
# CHECKOUT
# -------------------------------------------------------
@app.route("/checkout", methods=["POST"])
@login_required
def checkout():
    selected_item_ids = request.form.getlist("selected_items")
    name = request.form.get("name")
    address = request.form.get("address")
    contact = request.form.get("contact")

    if not selected_item_ids:
        flash("Select items first.", "warning")
        return redirect(url_for("cart"))
    
    # Validate Philippine mobile number
    if not validate_ph_mobile_number(contact):
        flash("Please enter a valid Philippine mobile number (11 digits starting with 09).", "danger")
        return redirect(url_for("cart"))
    
    cart_items = Cart.query.filter(
        Cart.id.in_(selected_item_ids),
        Cart.user_id == session["user_id"]
    ).all()

    if not cart_items:
        flash("Invalid items.", "warning")
        return redirect(url_for("cart"))

   # Calculate totals
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    discount = subtotal * 0.10
    total = subtotal - discount

    order_id = f"ORD-{int(time.time())}"

    session[f"order_{order_id}"] = {
        "selected_item_ids": selected_item_ids,
        "cart_items": [
            {
                "product_id": item.product_id,
                "product_name": item.product.name,
                "quantity": item.quantity,
                "price": item.product.price,
                "subtotal": item.product.price * item.quantity
            }
            for item in cart_items
        ],
        "subtotal": subtotal,
        "discount": discount,
        "total": total,
        "shipping_info": {
            "name": name,
            "address": address,
            "contact": contact
        }
    }

    return redirect(url_for("payment", order_id=order_id))

# -------------------------------------------------------
# PAYMENT (Simulated)
# -------------------------------------------------------
def initiate_gcash_payment(amount, order_id, description):
    gcash_app_id = os.getenv('GCASH_APP_ID')
    gcash_app_secret = os.getenv('GCASH_APP_SECRET')
    return {'status': 'success', 'payment_id': f'gcash_{order_id}', 'redirect_url': f'https://gcash.com/pay/{order_id}'}

def initiate_paymaya_payment(amount, order_id, description):
    paymaya_secret_key = os.getenv('PAYMAYA_SECRET_KEY')
    return {'status': 'success', 'payment_id': f'paymaya_{order_id}', 'redirect_url': f'https://paymaya.com/pay/{order_id}'}

def complete_purchase(order_id, payment_method):
    order = session.get(f"order_{order_id}")
    if not order:
        return False

    # Create purchase records
    for item in order["cart_items"]:
        purchase = Purchase(
            user_id=session["user_id"],
            product_id=item["product_id"],
            quantity=item["quantity"],
            total_price=item["subtotal"],
            payment_method=payment_method,
            shipping_name=order["shipping_info"]["name"],
            shipping_address=order["shipping_info"]["address"],
            shipping_contact=order["shipping_info"]["contact"]
        )
        db.session.add(purchase)

    # Remove cart items
    cart_ids = order["selected_item_ids"]
    Cart.query.filter(Cart.id.in_(cart_ids), Cart.user_id == session["user_id"]).delete()

    db.session.commit()

    # Clear session
    session.pop(f"order_{order_id}", None)
    return True

@app.route("/payment/<order_id>", methods=["GET", "POST"])
@login_required
def payment(order_id):
    order = session.get(f"order_{order_id}")
    if not order:
        flash("Order not found.", "danger")
        return redirect(url_for("cart"))

    if request.method == "POST":
        method = request.form.get("payment_method")

        if method == "GCash":
            result = initiate_gcash_payment(order["total"], order_id, "Makeup Purchase")
        elif method == "PayMaya":
            result = initiate_paymaya_payment(order["total"], order_id, "Makeup Purchase")
        elif method == "Cash on Delivery":
            if complete_purchase(order_id, "Cash on Delivery"):
                flash("Order placed successfully with Cash on Delivery.", "success")
                return redirect(url_for("home"))
            else:
                flash("Failed to complete order.", "danger")
                return redirect(url_for("payment", order_id=order_id))
        else:
            flash("Invalid payment method.", "danger")
            return redirect(url_for("payment", order_id=order_id))

        if result["status"] == "success":
            session[f"payment_{order_id}"] = {
                "payment_id": result["payment_id"],
                "method": method,
                "status": "pending"
            }
            return redirect(result["redirect_url"])

        flash("Payment failed to start.", "danger")
        return redirect(url_for("payment", order_id=order_id))

    return render_template("payment.html", order_data=order, order_id=order_id)

@app.route("/payment_success/<order_id>")
@login_required
def payment_success(order_id):
    payment_info = session.get(f"payment_{order_id}")
    if not payment_info:
        flash("Payment information not found.", "danger")
        return redirect(url_for("home"))

    if complete_purchase(order_id, payment_info["method"]):
        session.pop(f"payment_{order_id}", None)
        flash("Payment successful! Order completed.", "success")
        return redirect(url_for("home"))
    else:
        flash("Failed to complete order after payment.", "danger")
        return redirect(url_for("payment", order_id=order_id))

# -------------------------------------------------------
# ADMIN ROUTES
# -------------------------------------------------------
@app.route("/admin")
@admin_required
def admin():
    users = User.query.all()
    products = Product.query.all()
    tutorials = Tutorial.query.all()
    purchases = Purchase.query.all()
    histories = History.query.order_by(History.created_at.desc()).limit(10).all()
    return render_template("admin.html", users=users, products=products,
                           tutorials=tutorials, purchases=purchases,
                           histories=histories)

@app.route("/admin/users")
@admin_required
def admin_users():
    users = User.query.all()
    return render_template("admin_users.html", users=users)

@app.route("/edit_user", methods=["POST"])
@admin_required
def edit_user():
    user_id = request.form.get("user_id")
    user = User.query.get_or_404(user_id)
    user.name = request.form.get("name")
    user.email = request.form.get("email")
    db.session.commit()
    flash("User updated.", "success")
    return redirect(url_for("admin_users"))

@app.route("/toggle_admin/<int:user_id>", methods=["POST"])
@admin_required
def toggle_admin(user_id):
    user = User.query.get_or_404(user_id)
    user.is_admin = not user.is_admin
    db.session.commit()
    flash("Admin status changed.", "success")
    return redirect(url_for("admin_users"))

# PRODUCTS
@app.route("/admin/products")
@admin_required
def admin_products():
    products = Product.query.all()
    return render_template("admin_products.html", products=products)

@app.route("/add_product", methods=["POST"])
@admin_required
def add_product():
    new_product = Product(
        name=request.form.get("name"),
        description=request.form.get("description"),
        price=float(request.form.get("price")),
        category=request.form.get("category"),
        image_url=request.form.get("image_url")
    )
    db.session.add(new_product)
    db.session.commit()
    flash("Product added.", "success")
    return redirect(url_for("admin_products"))

@app.route("/edit_product", methods=["POST"])
@admin_required
def edit_product():
    product = Product.query.get_or_404(request.form.get("product_id"))
    product.name = request.form.get("name")
    product.description = request.form.get("description")
    product.price = float(request.form.get("price"))
    product.category = request.form.get("category")
    product.image_url = request.form.get("image_url")
    db.session.commit()

    flash("Product updated.", "success")
    return redirect(url_for("admin_products"))

@app.route("/delete_product/<int:product_id>", methods=["POST"])
@admin_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash("Product deleted.", "success")
    return redirect(url_for("admin_products"))

# TUTORIALS
@app.route("/admin/tutorials")
@admin_required
def admin_tutorials():
    tutorials = Tutorial.query.all()
    return render_template("admin_tutorials.html", tutorials=tutorials)

@app.route("/add_tutorial", methods=["POST"])
@admin_required
def add_tutorial():
    new_tutorial = Tutorial(
        title=request.form.get("title"),
        description=request.form.get("description"),
        category=request.form.get("category"),
        difficulty=request.form.get("difficulty"),
        duration=int(request.form.get("duration")),
        steps=request.form.get("steps"),
        user_id=session["user_id"]
    )
    db.session.add(new_tutorial)
    db.session.commit()
    flash("Tutorial added.", "success")
    return redirect(url_for("admin_tutorials"))

@app.route("/edit_tutorial", methods=["POST"])
@admin_required
def edit_tutorial():
    tutorial_id = request.form.get("tutorial_id")
    t = Tutorial.query.get_or_404(tutorial_id)
    t.title = request.form.get("title")
    t.description = request.form.get("description")
    t.category = request.form.get("category")
    t.difficulty = request.form.get("difficulty")
    t.duration = int(request.form.get("duration"))
    t.steps = request.form.get("steps")
    db.session.commit()

    flash("Tutorial updated.", "success")
    return redirect(url_for("admin_tutorials"))

@app.route("/delete_tutorial/<int:tutorial_id>", methods=["POST"])
@admin_required
def delete_tutorial(tutorial_id):
    tutorial = Tutorial.query.get_or_404(tutorial_id)
    db.session.delete(tutorial)
    db.session.commit()
    flash("Tutorial deleted.", "success")
    return redirect(url_for("admin_tutorials"))

# -------------------------------------------------------
# PROFILE
# -------------------------------------------------------
@app.route("/profile")
@login_required
def profile():
    user = User.query.get(session["user_id"])
    history = History.query.filter_by(
        user_id=session["user_id"]
    ).order_by(History.created_at.desc()).limit(10).all()

    purchases = Purchase.query.filter_by(
        user_id=session["user_id"]
    ).order_by(Purchase.created_at.desc()).all()

    return render_template("profile.html", user=user, history=history, purchases=purchases)

@app.route("/delete_history/<int:history_id>", methods=["POST"])
@login_required
def delete_history(history_id):
    h = History.query.get_or_404(history_id)
    if h.user_id != session["user_id"]:
        flash("Unauthorized.", "danger")
        return redirect(url_for("profile"))

    db.session.delete(h)
    db.session.commit()
    flash("History deleted.", "success")
    return redirect(url_for("profile"))

@app.route("/tutorial/step/<int:tutorial_id>")
@login_required
def tutorial_step(tutorial_id):
    tutorial = Tutorial.query.get_or_404(tutorial_id)

    # Example: if steps are stored in DB as a single text block separated by new lines
    steps = tutorial.steps.split("\n") if tutorial.steps else []

    # If you have images stored as comma-separated URLs
    step_images = tutorial.step_images.split(",") if tutorial.step_images else []

    return render_template(
        "tutorial_step.html",
        tutorial=tutorial,
        steps=steps,
        step_images=step_images
    )

@app.route("/rate_purchase/<int:purchase_id>", methods=["POST"])
@login_required
def rate_purchase(purchase_id):
    p = Purchase.query.get_or_404(purchase_id)

    if p.user_id != session["user_id"]:
        flash("Unauthorized.", "danger")
        return redirect(url_for("profile"))

    rating = request.form.get("rating")
    received_status = request.form.get("received_status")

    if rating:
        p.rating = int(rating)

    if received_status == "received":
        p.received = True
    elif received_status == "not_received":
        p.received = False

    db.session.commit()
    flash("Purchase updated.", "success")
    return redirect(url_for("profile"))

if __name__ == "__main__":
    app.run(debug=True)