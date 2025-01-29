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
   driver.execute_script("window.scrollBy(0,500);")
   title = driver.execute_script("return document.title")
   current_URL = driver.execute_script("return document.URL")
   print(title)
   print(current_URL)
   time.sleep(3)
   driver.quit()





