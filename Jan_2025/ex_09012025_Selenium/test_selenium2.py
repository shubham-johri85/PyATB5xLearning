from selenium import webdriver
import allure
import pytest
import time


@allure.title("login to app.vwo.com")
@pytest.mark.smoke
def test_vwo_login():
    driver = webdriver.Chrome()
    """
    1- This code is translated into the API request
    2- POST request-->Browser driver(Server)
    3- where it will create a fresh copy browser(Chrome)
    4- Session id - 6ac4667a25980f0425a477619e9374f8..16 digit will be created
    """
    driver.get("https://app.vwo.com")
    print(driver.session_id)
    """
    5- GET - GET API request to navigate to particular page
    6- browser will navigate to the URL
    """
    # Source Code(client)-->API Request(W3C)-->Browser Driver(Server)-->Browser
    time.sleep(15)
