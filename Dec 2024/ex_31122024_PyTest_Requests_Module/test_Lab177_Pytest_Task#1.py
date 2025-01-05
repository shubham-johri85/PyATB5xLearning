"""
Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.
"""

import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"
headers = {
    "Content-Type": "application/json"
}

def get_booking_id():

    base_path = "/booking"
    full_url = base_url + base_path
    payload = {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
   }
    response_data = requests.post(url=full_url,headers=headers,json=payload)

    assert response_data.status_code == 200

    response_data_json = response_data.json()
    booking_id = response_data_json["bookingid"]
    return booking_id


def get_token():
    base_path = "/auth"
    full_url = base_url + base_path
    json_payload = {
    "username" : "admin",
    "password" : "password123"
}
    response = requests.post(url=full_url,headers=headers,json=json_payload)
    response_json=response.json()
    token = response_json["token"]
    return token


def test_delete_booking():
    bookingid = get_booking_id()
    token = get_token()
    Delete_path = "/booking/" + str(bookingid)
    full_Delete_url = base_url+Delete_path
    cookie = "token="+token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    print(bookingid)
    print(token)
    response_delete = requests.delete(url=full_Delete_url,headers=headers)
    assert response_delete.status_code == 201

def test_deleted_bookingid():
    token = get_token()
    url = "https://restful-booker.herokuapp.com/booking/booking/2973"
    cookie = "token=" + token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    response_get = requests.get(url=url,headers=headers)
    assert response_get.status_code == 404






