from selenium import webdriver
import allure
import pytest
import time


@allure.title("verify the tile of app.vwo.com")
@pytest.mark.smoke
def test_vwo_login():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    print(driver.current_url)
    print(driver.page_source)
