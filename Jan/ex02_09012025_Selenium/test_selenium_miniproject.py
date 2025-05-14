from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os


@allure.title("verify CURA Healthcare Service available on Katalon cura website")
@pytest.mark.textverification
def test_Katalon_Text_Verification():
    driver = webdriver.Edge()
    driver.get(" https://katalon-demo-cura.herokuapp.com/#appointment")
    time.sleep(5)
    if "CURA Healthcare Service" in driver.page_source:
        print("Text Found, Passed")
    else:
        print("Text not available")
        pytest.fail("Text not available - Test case failed")

def test_Katalon_Invalid_Login():
    driver = webdriver.Chrome()
    driver.get(" https://katalon-demo-cura.herokuapp.com/#appointment")
    time.sleep(5)
    button = driver.find_element(By.ID, "btn-make-appointment")
    button.click()
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    driver.quit()



