import pytest
import requests
from dotenv import load_dotenv
import os

@pytest.fixture()
def create_token():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username,password)
    print("Creating token.....")
    full_url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url=full_url, headers=headers, json=json_payload)
    generated_token = response.json()["token"]
    return generated_token

@pytest.fixture()
def create_booking_id():
    print("Creating booking id!!!")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "firstname": "Shubham",
        "lastname": "Johri",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Lunch"
    }
    response_data = requests.post(url=URL, headers=headers, json=payload)
    booking_id = response_data.json()["bookingid"]
    return booking_id