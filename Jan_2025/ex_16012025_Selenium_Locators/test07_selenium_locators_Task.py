import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


@allure.title("Verify click button functionality")
@allure.description("click on login button and verify current url")
@pytest.mark.espocrm
def test_espocrm_login_click_TC01():
    firefox_options = Options()
    firefox_options.add_argument("--cognito")
    driver = webdriver.Chrome(firefox_options)
    driver.get("https://demo.us.espocrm.com")
    time.sleep(5)
    button_element = driver.find_element(By.ID, "btn-login")
    button_element.click()
    time.sleep(3)
    assert driver.current_url == "https://demo.us.espocrm.com/?l=en_US"
    time.sleep(5)
    driver.quit()

@allure.title("Verify click 'Advanced Pack' link")
@allure.description("click on 'Advanced Pack' link")
@pytest.mark.espocrm
def test_espocrm_AdvancedPack_click_TC02():
    firefox_options = Options()
    firefox_options.add_argument("--cognito")
    driver = webdriver.Chrome(firefox_options)
    driver.get("https://demo.us.espocrm.com")
    time.sleep(5)
    AP_element = driver.find_element(By.LINK_TEXT, "Advanced Pack")
    AP_element.click()
    time.sleep(5)
    driver.quit()


@allure.title("Verify click 'Sales Pack' link")
@allure.description("click on 'Sales Pack' link")
@pytest.mark.espocrm
def test_espocrm_SalesPack_click_TC03():
    firefox_options = Options()
    firefox_options.add_argument("--cognito")
    driver = webdriver.Chrome(firefox_options)
    driver.get("https://demo.us.espocrm.com")
    time.sleep(5)
    AP_element = driver.find_element(By.PARTIAL_LINK_TEXT, "Sales")
    AP_element.click()
    time.sleep(5)
    driver.quit()

@allure.title("Verify click 'Project Management' link")
@allure.description("click on 'Project Management' link")
@pytest.mark.espocrm
def test_espocrm_ProjectManagement_click_TC04():
    firefox_options = Options()
    firefox_options.add_argument("--cognito")
    driver = webdriver.Chrome(firefox_options)
    driver.get("https://demo.us.espocrm.com")
    time.sleep(5)
    AP_element = driver.find_element(By.LINK_TEXT, "Project Management")
    AP_element.click()
    time.sleep(5)
    driver.quit()