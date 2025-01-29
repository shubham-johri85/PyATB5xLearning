"""
https://demo.us.espocrm.com/

verify the title and current url

assert and create Allure HTML report also.
"""

from selenium import webdriver
import allure
import pytest
import time


@allure.title("Title and current URL verification")
@allure.description("verify the title and current url for - https://demo.us.espocrm.com/")
@pytest.mark.espocrm
def test_title_currentURL_espocrm():
    driver = webdriver.Firefox()
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(5)
    print(driver.title)
    print(driver.current_url)
    assert driver.title=="EspoCRM Demo"
    assert driver.current_url=="https://demo.us.espocrm.com/"
    driver.close()