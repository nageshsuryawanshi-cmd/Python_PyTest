import pytest
import requests
def test_get_users_endpoint():
    response = requests.get("https://typicode.com")
    assert response.status_code == 200