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

@allure.title("Actions on Window")
@allure.description("verify actions on Window")
def test_verify_actions_Window():
   load_dotenv()
   driver = webdriver.Firefox()
   driver.get(os.getenv("WINDOW_HANDLE"))
   driver.maximize_window()

   parent_window = driver.current_window_handle
   print(parent_window)
   link = driver.find_element(By.XPATH, "//a[@href='/windows/new']")
   link.click()
   window_handles = driver.window_handles
   print(window_handles)
   for handle in window_handles:
      driver.switch_to.window(handle)
      if "New Window" in driver.page_source:
         print("Action Passed")
         break

   driver.quit()






