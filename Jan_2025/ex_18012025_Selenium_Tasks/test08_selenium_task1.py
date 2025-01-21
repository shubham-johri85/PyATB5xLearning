"""
Open the Url - www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067

Search for the Macmini

Click on the search ICON

Get all the titles

Get al the prices

Print all the titles and prices in the end.
"""
import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os


def test_ebay_search():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("EBAY_URL"))
    search_element = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
    search_element.send_keys("Macmini")
    button_search = driver.find_element(By.CLASS_NAME, "gh-search-button__label")
    button_search.click()
    time.sleep(5)
    # assert driver.current_url == "https://www.ebay.com/sch/i.html?_nkw=Macmini&_sacat=0&_from=R40&_trksid=p4439441.m570.l1313"
    list_of_items = driver.find_elements(By.CSS_SELECTOR, ".s-item__title")
    list_of_items_prize = driver.find_elements(By.CSS_SELECTOR, ".s-item__price")

    for item, price in zip(list_of_items, list_of_items_prize):
        print(f"Item: {item.text}, Price: {price.text}")

    driver.quit()
