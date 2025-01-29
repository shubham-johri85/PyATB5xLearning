from selenium import webdriver
import allure
import pytest
import time


@allure.title("verify the tile of app.vwo.com")
@pytest.mark.smoke
def test_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"