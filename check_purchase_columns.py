from model import db
from app import app
from sqlalchemy import text

with app.app_context():
    print('Checking purchase table columns...')
    with db.engine.connect() as conn:
        result = conn.execute(text('DESCRIBE purchase'))
        columns = [row[0] for row in result]
        print('Columns:', columns)

        if 'payment_method' in columns:
            print('✅ payment_method column exists')
        else:
            print('❌ payment_method column missing - running migration...')
            conn.execute(text('ALTER TABLE purchase ADD COLUMN payment_method VARCHAR(50) NOT NULL DEFAULT "Cash on Delivery"'))
            print('✅ payment_method column added')
