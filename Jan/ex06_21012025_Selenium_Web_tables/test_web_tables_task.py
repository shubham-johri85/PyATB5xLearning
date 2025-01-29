from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import  time

"""
Web Tables 

https://awesomeqa.com/hr/web/index.php/auth/login

username : admin 
Password : Hacker@4321

Find the first element in the Webtable which is Terminated and click on the delete button
"""
def test_web_tables_ohrm():
    load_dotenv()
    driver = webdriver.Firefox()
    driver.get(os.getenv("AWESOMEQA_LOGIN"))
    driver.maximize_window()
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[normalize-space(@class='oxd-form-actions orangehrm-login-action')]")
    username.send_keys(os.getenv("AWESOMEQA_USERNAME"))
    password.send_keys(os.getenv("AWESOMEQA_PASSWORD"))
    login_button.click()

    # table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")
    # row_table = table.find_elements(By.TAG_NAME, "tr")
    #
    #
    #
    # for row in row_table:
    #     cols = row.find_elements(By.TAG_NAME, "td")
    #     for e in cols:
    #         print(e.text)

    driver.quit()
