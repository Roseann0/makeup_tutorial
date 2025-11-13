# TODO: Implement Cart Functionality for Makeup Tutorial Shop

## Step 1: Add Cart Model
- Add Cart model to model.py with fields: id, user_id, product_id, quantity, added_at

## Step 2: Update app.py with Cart Routes
- Add /add_to_cart/<product_id> route (POST) to add items to cart
- Add /cart route (GET) to view cart
- Add /remove_from_cart/<cart_id> route (POST) to remove items
- Add /checkout route (POST) to process purchases from cart
- Update /logout to clear cart on logout

## Step 3: Update Shop Template
- Change shop.html to have "Add to Cart" buttons instead of "Buy Now"
- Remove quantity input from shop, add it to cart page

## Step 4: Create Cart Template
- Create templates/cart.html to display cart items, quantities, totals, and checkout button

## Step 5: Update Navigation
- Add cart icon with item count to base.html navigation

## Step 6: Test Functionality
- Test adding items to cart
- Test viewing cart
- Test removing items
- Test checkout process
- Ensure cart clears on logout
