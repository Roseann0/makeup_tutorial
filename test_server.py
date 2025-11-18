import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://localhost:5000/')
    print(f"Status: {response.status}")
    content = response.read()
    print(f"Content length: {len(content)}")
    print(f"Content preview: {content[:200].decode('utf-8')}...")
except urllib.error.URLError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
