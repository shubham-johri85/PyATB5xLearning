"""
Automation for the Registration Page of the AwesomeQA.com/UI

Open - https://awesomeqa.com/ui/index.php?route=account/register

Fill the form

Verify that next page give - Your Account Has Been Created!
"""

import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv
import os

def test_awesomeqa_registration():
    load_dotenv()
    firefox_options = Options()
    firefox_options.add_argument("--incognito")
    driver = webdriver.Chrome(firefox_options)
    driver.get(os.getenv("AWESOMEQA_REGISTRATION"))
    time.sleep(3)
    firstname = driver.find_element(By.XPATH, "//input[@id='input-firstname']")
    firstname.send_keys(os.getenv("FIRSTNAME"))
    lastname = driver.find_element(By.XPATH, "//input[@id='input-lastname']")
    lastname.send_keys(os.getenv("LASTNAME"))
    email = driver.find_element(By.XPATH, "//input[@id='input-email']")
    email.send_keys(os.getenv("EMAIL"))
    telephone = driver.find_element(By.XPATH, "//input[@id='input-telephone']")
    telephone.send_keys(os.getenv("TELEPHONE"))
    password = driver.find_element(By.XPATH, "//input[@id='input-password']")
    password.send_keys(os.getenv("PASSWORD_AQA"))
    confirm = driver.find_element(By.XPATH, "//input[@id='input-confirm']")
    confirm.send_keys(os.getenv("PASSWORD_CONFIRM_AQA"))
    checkbox_click = driver.find_element(By.XPATH, "//input[@name='agree']")
    checkbox_click.click()
    submit = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit.click()
    time.sleep(3)
    assert driver.current_url == "https://awesomeqa.com/ui/index.php?route=account/success"
    message = driver.find_element(By.ID, "content")
    assert "Your Account Has Been Created!" in message.text
    driver.quit()
