from model import db
from app import app

with app.app_context():
    # Add payment_method column to purchase table
    db.engine.execute('ALTER TABLE purchase ADD COLUMN payment_method VARCHAR(50) NOT NULL DEFAULT "Cash on Delivery"')
    print("Added payment_method column to purchase table")
