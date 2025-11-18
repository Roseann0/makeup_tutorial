import requests
import time

time.sleep(2)

try:
    response = requests.get('http://127.0.0.1:5000/', timeout=10)
    print(f'Success: {response.status_code}')
    print('Response text:', response.text[:200])
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
