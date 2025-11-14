from model import db, User
from app import app
from sqlalchemy import text

with app.app_context():
    # Add is_admin column to User table if it doesn't exist
    try:
        db.session.execute(text("ALTER TABLE user ADD COLUMN is_admin BOOLEAN DEFAULT FALSE"))
        print("Added is_admin column to user table.")
    except Exception as e:
        print(f"Column might already exist or error: {e}")

    # Commit any changes
    db.session.commit()
    print("Database migration completed.")
