import allure
import pytest
import requests

@allure.title("verify the GET Request of Restful Booker")
@allure.description("This is to test the Booking 1 and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    url_get = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url_get)
    # print(response_data.json())
    assert response_data.status_code == 200


@allure.title("verify the GET Request of Restful Booker for negative scenario")
@allure.description("This is to test the Booking -1 and verify the response")
@pytest.mark.negative
def test_get_request_negative():
    url_get = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=url_get)
    # print(response_data.json())
    assert response_data.status_code == 404
