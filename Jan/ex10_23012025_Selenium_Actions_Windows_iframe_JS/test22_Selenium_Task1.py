"""
Navigate to the URL - https://www.spicejet.com/

Enter the Del and hit tab, BLR

By using the Action class. (chain)
"""

import allure
import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

@allure.title("Test SpiceJet actions")
@allure.description("Verify keyboard actions on SpiceJet")
def test_spicejet_actions():
    load_dotenv()
    # chrome_options = Options()
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--disable-geolocation")
    # chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Firefox()
    driver.get(os.getenv("SPICEJET"))
    driver.maximize_window()
    pyautogui.press('tab')
    pyautogui.press('enter')
    fromcity = driver.find_element(By.XPATH, "//div[@id='main-container']//div[3]//div[2]//div[3]//div//div[1]//div//div[2]//input")
    tocity = driver.find_element(By.XPATH, "//div[@id='main-container']//div[3]//div[2]//div[3]//div//div[3]//div[1]//div[2]//input")
    actions = ActionChains(driver=driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(fromcity, "DEL").key_up(Keys.SHIFT).perform()
    actions.key_down(Keys.TAB).perform()
    actions.key_down(Keys.SHIFT).send_keys_to_element(tocity, "BLR").key_up(Keys.SHIFT).perform()
    time.sleep(10)
    driver.quit()
