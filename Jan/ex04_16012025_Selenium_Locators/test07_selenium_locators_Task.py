import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv
import os

@allure.title("Verify click button functionality")
@allure.description("click on login button and verify current url")
@pytest.mark.espocrm
def test_espocrm_login_click_tc01():
    load_dotenv()
    firefox_options = Options()
    firefox_options.add_argument("--cognito")
    driver = webdriver.Chrome(firefox_options)
    driver.get(os.getenv("URLESPOCRM"))
    time.sleep(5)
    button_element = driver.find_element(By.ID, "btn-login")
    button_element.click()
    time.sleep(3)
    assert driver.current_url == os.getenv("URLESPOCRM_LOGIN_CLICK")
    time.sleep(5)
    driver.quit()

@allure.title("Verify click 'Advanced Pack' link")
@allure.description("click on 'Advanced Pack' link")
@pytest.mark.espocrm
def test_espocrm_advancedpack_click_tc02():
    load_dotenv()
    firefox_options = Options()
    firefox_options.add_argument("--cognito")
    driver = webdriver.Chrome(firefox_options)
    driver.get(os.getenv("URLESPOCRM"))
    time.sleep(5)
    ap_element = driver.find_element(By.LINK_TEXT, "Advanced Pack")
    ap_element.click()
    time.sleep(5)
    driver.quit()


@allure.title("Verify click 'Sales Pack' link")
@allure.description("click on 'Sales Pack' link")
@pytest.mark.espocrm
def test_espocrm_salespack_click_tc03():
    load_dotenv()
    firefox_options = Options()
    firefox_options.add_argument("--cognito")
    driver = webdriver.Chrome(firefox_options)
    driver.get(os.getenv("URLESPOCRM"))
    time.sleep(5)
    sp_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Sales")
    sp_element.click()
    time.sleep(5)
    driver.quit()

@allure.title("Verify click 'Project Management' link")
@allure.description("click on 'Project Management' link")
@pytest.mark.espocrm
def test_espocrm_projectmanagement_click_tc04():
    load_dotenv()
    firefox_options = Options()
    firefox_options.add_argument("--cognito")
    driver = webdriver.Chrome(firefox_options)
    driver.get(os.getenv("URLESPOCRM"))
    time.sleep(5)
    pm_element = driver.find_element(By.LINK_TEXT, "Project Management")
    pm_element.click()
    time.sleep(5)
    driver.quit()