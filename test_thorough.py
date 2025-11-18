import requests
import json
from app import app, db
from model import Tutorial, User

def test_tutorial_routes():
    with app.test_client() as client:
        # Test tutorial page
        response = client.get('/tutorial')
        print(f"Tutorial page status: {response.status_code}")
        assert response.status_code == 200

        # Test tutorial detail page
        tutorial = Tutorial.query.first()
        if tutorial:
            response = client.get(f'/tutorial/{tutorial.id}')
            print(f"Tutorial detail status: {response.status_code}")
            assert response.status_code == 200
            assert b'Step-by-Step Tutorial' in response.data
            assert b'Video Tutorial' in response.data

            # Test step-by-step route
            response = client.get(f'/tutorial/{tutorial.id}/step')
            print(f"Step-by-step status: {response.status_code}")
            assert response.status_code == 200
            assert b'Step-by-Step Guide' in response.data

            # Test video route
            response = client.get(f'/tutorial/{tutorial.id}/video')
            print(f"Video tutorial status: {response.status_code}")
            assert response.status_code == 200
            assert b'Video Tutorial' in response.data

        print("All tutorial routes tested successfully!")

if __name__ == '__main__':
    with app.app_context():
        test_tutorial_routes()
