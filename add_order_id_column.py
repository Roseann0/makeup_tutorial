from model import db
from app import app

with app.app_context():
    # Add order_id column to purchase table
    with db.engine.connect() as conn:
        conn.execute(db.text("ALTER TABLE purchase ADD COLUMN order_id VARCHAR(50)"))
        conn.commit()
    print("Added order_id column to purchase table.")
