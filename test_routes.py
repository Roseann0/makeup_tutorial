import requests

base_url = 'http://127.0.0.1:5000'

print("Testing tutorial and shop routes...")

# Test tutorial route without login (should redirect)
r = requests.get(f'{base_url}/tutorial')
print(f'Tutorial route without login: {r.status_code} - {r.url}')

# Test shop route without login (should redirect)
r = requests.get(f'{base_url}/shop')
print(f'Shop route without login: {r.status_code} - {r.url}')

# Test cart route without login (should redirect)
r = requests.get(f'{base_url}/cart')
print(f'Cart route without login: {r.status_code} - {r.url}')

print("All routes tested. They should redirect to login since no session.")
