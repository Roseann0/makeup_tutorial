from model import db
from app import app
from sqlalchemy import text

with app.app_context():
    # Add shipping columns to Purchase table
    db.session.execute(text('ALTER TABLE purchase ADD COLUMN shipping_name VARCHAR(100)'))
    db.session.execute(text('ALTER TABLE purchase ADD COLUMN shipping_address TEXT'))
    db.session.execute(text('ALTER TABLE purchase ADD COLUMN shipping_contact VARCHAR(20)'))
    db.session.commit()
    print("Shipping columns added to Purchase table.")
