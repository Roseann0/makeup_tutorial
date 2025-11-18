from app import app, db, Product

with app.app_context():
    # Dictionary of product names to new prices
    price_updates = {
        'Foundation Brush': 299.00,
        'Lipstick - Ruby Red': 395.00,
        'Eyeshadow Palette': 857.00,
        'Mascara': 299.00,
        'Blush - Peachy Pink': 325.00,
        'Highlighter': 499.00,
        'Eyeliner Pencil': 299.00,
        'Setting Powder': 399.00,
        'Bronzer': 249.00,
        'Lip Gloss': 299.00
    }

    products = Product.query.all()
    updated_count = 0

    for product in products:
        if product.name in price_updates:
            product.price = price_updates[product.name]
            updated_count += 1
            print(f"Updated {product.name}: ₱{product.price}")

    db.session.commit()
    print(f"\nTotal products updated: {updated_count}")
