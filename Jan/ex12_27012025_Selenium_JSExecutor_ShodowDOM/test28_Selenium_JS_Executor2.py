import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionBuilder, ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("JS Executor")
@allure.description("verify scroll")
def test_verify_js_scroll():
   load_dotenv()
   driver = webdriver.Firefox()
   driver.get(os.getenv("selectorhub"))
   username_div = driver.find_element(By.XPATH, "//*[@id='userName']")
   driver.execute_script("arguments[0].scrollIntoView(true);", username_div)
   time.sleep(3)
   driver.quit()





