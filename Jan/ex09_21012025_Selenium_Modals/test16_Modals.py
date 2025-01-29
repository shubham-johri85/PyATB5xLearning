from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_modals_html_css():
    load_dotenv()
    driver = webdriver.Firefox()
    driver.get(os.getenv("MAKEMYTRIP"))
    WebDriverWait(driver=driver, timeout=3).until(EC.visibility_of_element_located((By.CLASS_NAME, "commonModal__close")))
    modal = driver.find_element(By.CLASS_NAME, "commonModal__close")
    modal.click()

    driver.quit()

