from selenium import webdriver
import allure
import pytest
import time


def test_katalon_firefox():
    driver = webdriver.Firefox()
    driver.get(" https://katalon-demo-cura.herokuapp.com/#appointment")
    time.sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    # driver.close() # close current window(tab)
    driver.quit() #close complete browser(all tabs)