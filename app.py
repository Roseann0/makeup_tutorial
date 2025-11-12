import os
import re
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from functools import wraps
from model import db, User  # make sure your file is named model.py

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
    tutorials = [
        {'title': 'Clean Girl Make-up', 'desc': 'Simple natural daily look.'},
        {'title': 'DuoYin Make-up', 'desc': 'Chinese makeup style that looks like a doll.'},
    ]
    return render_template('tutorial.html', tutorials=tutorials)

# ---------------- DESCRIPTION ----------------
@app.route('/description')
@login_required
def description():
    suggestions = {
        'tones': ['Fair', 'Medium', 'Tan', 'Deep'],
        'tips': [
            'Dry skin: Use hydrating primer and cream foundation.',
            'Oily skin: Try mattifying primer and oil-control powder.',
            'Warm undertone: Choose peach/golden shades.',
            'Cool undertone: Choose pink/rosy shades.'
        ]
    }
    return render_template('description.html', suggestions=suggestions)

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
