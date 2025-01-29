import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.webdriver.support.ui import Select
import os

@allure.title("Froms filling validation")
@allure.description("Verify filling of form and submit")
@pytest.mark.awesomeqa
def test_input_radio_checkbox():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("AWESOMEQA_PRACTICE"))
    firstname = driver.find_element(By.NAME, "firstname")
    firstname.send_keys("Shubham")
    lastname = driver.find_element(By.NAME, "lastname")
    lastname.send_keys("Johri")
    gender =  driver.find_element(By.XPATH, "//input[@id='sex-1']")
    gender.click()
    experience =  driver.find_element(By.XPATH, "//input[@id='exp-2']")
    experience.click()
    date = driver.find_element(By.ID, "datepicker")
    date.send_keys("21/02/1985")
    profession =  driver.find_element(By.XPATH, "//input[@id='profession-1']")
    profession.click()
    tool =  driver.find_element(By.ID, "tool-2")
    tool.click()
    continents = driver.find_element(By.XPATH, "//select[@id='continents']")
    select = Select(continents)
    select.select_by_index(5)
    commands = driver.find_element(By.XPATH, "//select[@id='selenium_commands']")
    select = Select(commands)
    select.select_by_index(3)
    time.sleep(5)
    driver.quit()