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

@allure.title("Actions on MakeMyTrip")
@allure.description("verify actions on MakeMyTrip")
def test_verify_actions_MakeMyTrip():
   load_dotenv()
   driver = webdriver.Firefox()
   driver.get(os.getenv("MAKEMYTRIP"))
   driver.maximize_window()
   WebDriverWait(driver=driver, timeout=3).until(EC.visibility_of_element_located((By.CLASS_NAME, "commonModal__close")))
   modal = driver.find_element(By.CLASS_NAME, "commonModal__close")
   modal.click()
   fromcity = driver.find_element(By.XPATH,"//input[@id='fromCity']")
   actions = ActionChains(driver=driver)
   actions.move_to_element(fromcity).click().send_keys("del").perform()
   time.sleep(3)
   actions.move_to_element(fromcity).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
   allure.attach(driver.get_screenshot_as_png(), name="test_verify_actions_MakeMyTrip-screenshot", attachment_type=AttachmentType.PNG)
   driver.quit()





