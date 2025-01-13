import pytest
import allure
import requests


base_url = "https://restful-booker.herokuapp.com"
headers = {
    "Content-Type": "application/json"
}

@allure.title("TC01-Create token CRUD positive")
@allure.description("Verify the token is created")
@pytest.mark.crud
def test_create_token_positive_tc01():
    base_path = "/auth"
    full_url = base_url + base_path
    json_payload = {
    "username" : "admin",
    "password" : "password123"
}
    response = requests.post(url=full_url,headers=headers,json=json_payload)
    assert response.status_code == 200
    response_json=response.json()
    token = response_json["token"]
    print(token)
    assert token is not None
    assert type(token) == str

