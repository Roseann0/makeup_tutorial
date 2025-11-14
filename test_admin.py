from app import app, db
from model import User, Product, Tutorial

with app.app_context():
    # Test admin user exists
    admin = User.query.filter_by(email='admin@makeuptutorial.com').first()
    if admin:
        print(f"Admin user found: ID {admin.id}, Name: {admin.name}, Admin: {admin.is_admin}")
    else:
        print("Admin user not found!")

    # Test products
    products = Product.query.all()
    print(f"Total products: {len(products)}")

    # Test tutorials
    tutorials = Tutorial.query.all()
    print(f"Total tutorials: {len(tutorials)}")

    # Test all users
    users = User.query.all()
    print(f"Total users: {len(users)}")
    for user in users:
        print(f"  User {user.id}: {user.name} ({user.email}) - Admin: {user.is_admin}")
