from model import db, Purchase
from flask import Flask
from dotenv import load_dotenv
import os
from sqlalchemy import text

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://rose:makeuptutorial@127.0.0.1/makeup_tutorial'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    # Add the new columns to the Purchase table
    with db.engine.connect() as conn:
        conn.execute(text('ALTER TABLE purchase ADD COLUMN rating INTEGER DEFAULT NULL'))
        conn.execute(text('ALTER TABLE purchase ADD COLUMN received BOOLEAN DEFAULT FALSE'))
        conn.commit()
    print("Columns added successfully!")
