from selenium import webdriver
import allure
import pytest
import time


@allure.title("verify CURA Healthcare Service available on Katalon cura website")
@pytest.mark.textverification
def test_Katalon_Text_Verification():
    driver = webdriver.Edge()
    driver.get(" https://katalon-demo-cura.herokuapp.com/#appointment")
    if "PURA Healthcare Service" in driver.page_source:
        print("Text Found, Passed")
    else:
        print("Text not available")
        pytest.fail("Text not available - Test case failed")

