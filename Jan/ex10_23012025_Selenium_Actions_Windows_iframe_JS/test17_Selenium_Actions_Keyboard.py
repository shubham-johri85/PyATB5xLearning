import allure
import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@allure.title("Actions P1")
@allure.description("verify actions P1")
def test_verify_action_keyboard():
   load_dotenv()
   driver = webdriver.Firefox()
   driver.get(os.getenv("ACTIONSURL_KEYBOARD"))
   first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
   actions = ActionChains(driver=driver) # crated object of an action
   (actions.key_down(Keys.SHIFT)
    .send_keys_to_element(first_name, "shubham testing 123")
    .key_up(Keys.SHIFT)
    .perform())
   time.sleep(10)
   driver.quit()





