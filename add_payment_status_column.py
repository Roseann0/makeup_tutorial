from model import db, Purchase
from app import app

with app.app_context():
    # Add payment_status column to Purchase table
    with db.engine.connect() as conn:
        conn.execute(db.text("ALTER TABLE purchase ADD COLUMN payment_status VARCHAR(50) DEFAULT 'pending'"))
        conn.commit()
    print("Added payment_status column to Purchase table.")
