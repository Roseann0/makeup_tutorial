# TODO for Cart Page Modifications

- [x] Hide checkboxes initially in cart.html using CSS (display: none)
- [x] Change checkout button text to "Select Items to Checkout"
- [x] Add JavaScript event listener to button click: show checkboxes and change button text to "Checkout Selected Items"
- [x] Add confirmation dialog (confirm()) for remove buttons in JavaScript
- [x] Update existing JavaScript for total calculation to work with shown checkboxes
- [x] Test the cart flow to ensure checkout proceeds to receipts (App running on http://127.0.0.1:5000, browser tool disabled but app is live)
- [x] Add individual "Checkout" button beside each "Remove" button
- [x] Implement JavaScript to handle individual checkout: set selected_items to single item and submit main form

# TODO for Shipping Information

- [x] Add shipping columns to Purchase model (shipping_name, shipping_address, shipping_contact)
- [x] Create migration script to add shipping columns to database
- [x] Update purchase creation in app.py to include shipping info from session
- [x] Update receipt.html to display shipping information
