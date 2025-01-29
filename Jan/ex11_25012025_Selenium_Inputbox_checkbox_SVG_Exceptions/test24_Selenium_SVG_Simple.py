import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from selenium.webdriver.support.ui import Select
import os


@allure.title("SVG validation")
@allure.description("Verify svg")
@pytest.mark.flipkart
def test_svg_flipkart():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("FLIPKART"))
    searchbox = driver.find_element(By.NAME, "q")
    searchbox.send_keys("macmini")
    time.sleep(5)
    list_svg_element = driver.find_elements(By.XPATH, "//*[name()='svg']")
    list_svg_element[0].click()

    driver.quit()
