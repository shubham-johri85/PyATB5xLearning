from selenium import webdriver
import allure
import pytest
import time


@allure.title("login to app.vwo.com")
@pytest.mark.smoke
def test_vwo_login1():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    time.sleep(15)


def test_vwo_login2():
    driver = webdriver.Firefox()
    driver.get("https://app.vwo.com")
    time.sleep(15)


def test_vwo_login3():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    time.sleep(15)
