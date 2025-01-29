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

@allure.title("Verify Iframe")
@allure.description("verify actions on iframe")
def test_verify_action_iframe():
   load_dotenv()
   driver = webdriver.Firefox()
   driver.get(os.getenv("IFRAME"))
   driver.maximize_window()
   time.sleep(5)
   main_window_handle = driver.current_window_handle
   list = driver.find_elements(By.CSS_SELECTOR, "[data-qa=yedexafobi]")
   variation = list[1]
   actions = ActionChains(driver=driver) # crated object of an action
   actions.click(variation).perform()
   time.sleep(15)
   all_handle = driver.window_handles
   for handle in all_handle:
      if handle !=main_window_handle:
       driver.switch_to.window(handle)
       print(driver.title)
       driver.switch_to.frame("heatmap-iframe")
       clickmap = driver.find_element(By.CSS_SELECTOR, "[data-qa=liqokuxuba]")
       clickmap.click()
       time.sleep(20)

   time.sleep(5)
   driver.quit()






