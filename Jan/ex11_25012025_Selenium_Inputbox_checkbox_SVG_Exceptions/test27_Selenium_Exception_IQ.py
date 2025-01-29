import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from selenium.common.exceptions import StaleElementReferenceException
import os


@allure.title("Exception validation")
@allure.description("Verify Exception")
def test_exception():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("GOOGLE"))
    element = driver.find_element(By.NAME, "q")
    driver.refresh()
    try:
     element.send_keys("The Rock")
    except StaleElementReferenceException as sere:
        print(sere.msg)
        print("StaleElementReferenceException")

    time.sleep(3)
