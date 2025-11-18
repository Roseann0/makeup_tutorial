from app import app, db
from model import User
from werkzeug.security import check_password_hash

with app.app_context():
    # Test admin user exists
    user = User.query.filter_by(email='admin@makeuptutorial.com').first()
    print(f"Admin user found: {user.name if user else 'None'}")
    print(f"Is admin: {user.is_admin if user else 'N/A'}")

    # Test password check
    if user:
        valid = check_password_hash(user.password_hash, 'AdminPass123!')
        print(f"Password valid: {valid}")

    # Test invalid login
    invalid_user = User.query.filter_by(email='invalid@example.com').first()
    print(f"Invalid user found: {invalid_user.name if invalid_user else 'None'}")

    # Test tutorial exists
    from model import Tutorial
    tutorial = Tutorial.query.first()
    print(f"Tutorial found: {tutorial.title if tutorial else 'None'}")
