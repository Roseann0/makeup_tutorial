from app import app, db
from model import User
from werkzeug.security import generate_password_hash

with app.app_context():
    # Check if admin already exists
    admin = User.query.filter_by(email='admin@makeuptutorial.com').first()
    if admin:
        print("Admin user already exists.")
    else:
        # Create admin user
        hashed_password = generate_password_hash('AdminPass123!')
        admin_user = User(
            name='Admin',
            email='admin@makeuptutorial.com',
            password_hash=hashed_password,
            is_admin=True
        )
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created successfully!")
        print("Email: admin@makeuptutorial.com")
        print("Password: AdminPass123!")
