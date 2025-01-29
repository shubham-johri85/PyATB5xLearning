import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException
import os


@allure.title("Exception validation")
@allure.description("Verify Exception")
def test_exception_handle():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("AWESOMEQA_PRACTICE"))
    try:
       element = driver.find_element(By.ID, "element_not_available")
    except NoSuchElementException as nse:
        print(nse.msg)


    time.sleep(3)
