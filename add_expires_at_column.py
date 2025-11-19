from model import db, OTP
from app import app
from sqlalchemy import text
from datetime import datetime

with app.app_context():
    # Add expires_at column to OTP table if it doesn't exist
    try:
        # First, add the column with a default value
        db.session.execute(text("ALTER TABLE otp ADD COLUMN expires_at DATETIME NOT NULL DEFAULT (NOW() + INTERVAL 10 MINUTE)"))
        print("Added expires_at column to otp table.")
    except Exception as e:
        print(f"Column might already exist or error: {e}")

    # Commit any changes
    db.session.commit()
    print("Database migration completed.")
