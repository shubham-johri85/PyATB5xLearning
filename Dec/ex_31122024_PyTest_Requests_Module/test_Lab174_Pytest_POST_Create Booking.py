import pytest
import allure
import requests

@allure.title("TC01-Create booking CRUD positive")
@allure.description("Verify the create booking")
@pytest.mark.crud
def test_create_booking_positive_tc01():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_url = base_url + base_path
    headers = {
        "Content-Type" : "application/json"
    }
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
    print(booking_id)
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int

    firstname = response_data_json["booking"]["firstname"]
    assert firstname == "Jim"
    assert type(firstname) == str

    lastname = response_data_json["booking"]["lastname"]
    totalprice = response_data_json["booking"]["totalprice"]
    depositepaid = response_data_json["booking"]["depositpaid"]

    assert lastname == "Brown"
    assert type(lastname) == str
    assert totalprice == 111
    assert depositepaid == True

    Checkin_date = response_data_json["booking"]["bookingdates"]["checkin"]
    Checkout_date = response_data_json["booking"]["bookingdates"]["checkout"]

    assert Checkin_date == '2018-01-01'
    assert Checkout_date == '2019-01-01'

    time = response_data.elapsed.total_seconds()
    assert time < 3



@allure.title("TC02-Create booking CRUD negative")
@allure.description("Verify the booking is not created when invalid payload")
@pytest.mark.crud
def test_create_booking_negative_tc02():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_url = base_url + base_path
    headers = {
        "Content-Type" : "application/json"
    }
    json_payload ={}
    response = requests.post(url=full_url,headers=headers,json=json_payload)
    assert response.status_code == 500
    assert response.text == "Internal Server Error"

