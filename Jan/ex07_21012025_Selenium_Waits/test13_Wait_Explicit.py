import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_implicit_wait():
    load_dotenv()
    driver = webdriver.Firefox()
    driver.get(os.getenv("URL"))
    email_element = driver.find_element(By.ID, "login-username")
    email_element.send_keys(os.getenv("INVALID_USERNAME"))
    password_element = driver.find_element(By.ID, "login-password")
    password_element.send_keys(os.getenv("INVALID_PASSWORD"))
    button_element = driver.find_element(By.ID, "js-login-btn")
    button_element.click()
    WebDriverWait(driver, timeout=3).until(EC.visibility_of_element_located((By.CLASS_NAME,"notification-box-description")))#Explicit Wait
    error_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description" )
    print(error_web_element.text)
    assert error_web_element.text == os.getenv("ERROR_MESSAGE_EXPECTED")
    driver.quit()
