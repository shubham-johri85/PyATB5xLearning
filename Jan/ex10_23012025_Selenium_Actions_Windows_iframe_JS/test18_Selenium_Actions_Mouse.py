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

@allure.title("Actions P2")
@allure.description("verify actions P2")
def test_verify_action_mouse():
   load_dotenv()
   driver = webdriver.Firefox()
   driver.get(os.getenv("ACTIONURL_MOUSE"))
   atag = driver.find_element(By.ID, "click")
   atag.click()
   actions = ActionBuilder(driver=driver) # crated object of an action
   actions.pointer_action.pointer_up(MouseButton.BACK)
   actions.perform()
   time.sleep(10)
   driver.quit()





