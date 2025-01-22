import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os


def test_imp_wait():
    load_dotenv()
    driver = webdriver.Firefox()
    driver.get(os.getenv("URL"))
    driver.implicitly_wait(10) # Wait for 10 secends
    email_element = driver.find_element(By.ID, "login-username")
    email_element.send_keys(os.getenv("INVALID_USERNAME"))
    password_element = driver.find_element(By.ID, "login-password")
    password_element.send_keys(os.getenv("INVALID_PASSWORD"))
    driver.quit()
