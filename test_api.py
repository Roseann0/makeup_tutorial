import requests
import threading
import time

def run_app():
    from app import app
    app.run(debug=False, port=5000, use_reloader=False)

thread = threading.Thread(target=run_app, daemon=True)
thread.start()
time.sleep(3)

base_url = 'http://127.0.0.1:5000'

print('Starting comprehensive API testing...')

print('\n=== Testing Basic Routes ===')
response = requests.get(f'{base_url}/')
print(f'Index: {response.status_code}')

response = requests.get(f'{base_url}/register')
print(f'Register GET: {response.status_code}')

response = requests.get(f'{base_url}/login')
print(f'Login GET: {response.status_code}')

print('\n=== Testing Protected Routes Without Auth ===')
response = requests.get(f'{base_url}/home')
print(f'Home without auth: {response.status_code} - redirects to: {response.url}')

response = requests.get(f'{base_url}/tutorial')
print(f'Tutorial without auth: {response.status_code} - redirects to: {response.url}')

response = requests.get(f'{base_url}/shop')
print(f'Shop without auth: {response.status_code} - redirects to: {response.url}')

response = requests.get(f'{base_url}/admin')
print(f'Admin without auth: {response.status_code} - redirects to: {response.url}')

print('\n=== Testing User Registration ===')
data = {
    'name': 'testuser',
    'email': 'test@example.com',
    'password': 'TestPass123!'
}
response = requests.post(f'{base_url}/register', data=data, allow_redirects=False)
location = response.headers.get('Location', 'No redirect')
print(f'Register POST: {response.status_code} - Location: {location}')

print('\n=== Testing Login ===')
data = {
    'email': 'test@example.com',
    'password': 'TestPass123!'
}
response = requests.post(f'{base_url}/login', data=data, allow_redirects=False)
location = response.headers.get('Location', 'No redirect')
print(f'Login POST: {response.status_code} - Location: {location}')

print('\n=== Testing Invalid Login ===')
data = {
    'email': 'test@example.com',
    'password': 'WrongPass123!'
}
response = requests.post(f'{base_url}/login', data=data, allow_redirects=False)
location = response.headers.get('Location', 'No redirect')
print(f'Invalid Login POST: {response.status_code} - Location: {location}')

print('\nAPI testing completed.')
