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

@allure.title("Actions P3")
@allure.description("verify actions P3")
def test_verify_action_click_hold():
   load_dotenv()
   driver = webdriver.Firefox()
   driver.get(os.getenv("ACTIONURL_MOUSE"))
   element_to_hold = driver.find_element(By.ID, "draggable")

   actions = ActionChains(driver=driver) # crated object of an action
   actions.click_and_hold(on_element=element_to_hold).perform()

   time.sleep(10)
   driver.quit()





