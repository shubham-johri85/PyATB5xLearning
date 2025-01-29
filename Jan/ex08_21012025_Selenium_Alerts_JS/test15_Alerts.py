import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def test_alerts_js_normal():
    load_dotenv()
    driver = webdriver.Firefox()
    driver.get(os.getenv("ALERTS_JS"))
    button_element = driver.find_element(By.XPATH, "//button[normalize-space(@text='Click for JS Alert')]")
    button_element.click()
    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    result = driver.find_element(By.ID, "result")
    assert result.text == "You successfully clicked an alert"
    time.sleep(5)

def test_alerts_js_confirmation():
    load_dotenv()
    driver = webdriver.Firefox()
    driver.get(os.getenv("ALERTS_JS"))
    button_element = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    button_element.click()
    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.dismiss()
    result = driver.find_element(By.ID, "result")
    assert result.text == "You clicked: Cancel"
    time.sleep(5)

def test_alerts_js_prompt():
    load_dotenv()
    driver = webdriver.Firefox()
    driver.get(os.getenv("ALERTS_JS"))
    button_element = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    button_element.click()
    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Shubham")
    alert.accept()
    result = driver.find_element(By.ID, "result")
    assert result.text == "You entered: Shubham"
    time.sleep(5)
    driver.quit()

