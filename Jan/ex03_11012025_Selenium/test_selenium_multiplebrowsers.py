from selenium import webdriver
import allure
import pytest
import time


@allure.title("verify CURA Healthcare Service available on Katalon cura website")
@pytest.mark.textverification
def test_katalon_edge():
    driver = webdriver.Edge()
    driver.get(" https://katalon-demo-cura.herokuapp.com/#appointment")
    time.sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"


def test_katalon_chrome():
    driver = webdriver.Chrome()
    driver.get(" https://katalon-demo-cura.herokuapp.com/#appointment")
    time.sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"


def test_katalon_firefox():
    driver = webdriver.Firefox()
    driver.get(" https://katalon-demo-cura.herokuapp.com/#appointment")
    time.sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"