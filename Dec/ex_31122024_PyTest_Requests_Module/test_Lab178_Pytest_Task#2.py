"""
Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.
"""

import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"
headers = {
    "Content-Type": "application/json"
}

def get_booking_all():
    base_path = "/booking"
    full_url = base_url + base_path
    response_data = requests.get(url=full_url)
    return response_data

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

def test_Update_Patch_request(): # Update booking.
    bookingid = 797
    token = get_token()
    print(bookingid)
    print(token)
    base_path = "/booking/" + str(bookingid)
    full_patch_url = base_url+base_path
    cookie = "token="+token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    json_payload = {
    "firstname": "Updated by Patch request",
    "lastname": "Allen",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
   },
    "additionalneeds": "API Testing"
   }

    response = requests.patch(url=full_patch_url,headers=headers,json=json_payload)
    print(response.json()["firstname"])
    print(response.json()["additionalneeds"])
    assert response.status_code == 200
    assert response.json()["firstname"] == "Updated by Patch request"
    assert response.json()["additionalneeds"] == "API Testing"








