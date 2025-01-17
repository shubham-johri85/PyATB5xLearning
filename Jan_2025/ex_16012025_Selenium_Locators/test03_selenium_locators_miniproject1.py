import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os



def test_app_vwo_login_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com/#/login")
    """
    <
    input type="email" 
    class="text-input W(100%)" 
    name="username" 
    id="login-username" 
    data-qa="hocewoqisi">
    """
    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys("abc@abc.com")
    """
    <input type="password" 
    class="text-input W(100%)" 
    name="password" 
    id="login-password" 
    data-qa="jobodapuxe">
    """
    password_element = driver.find_element(By.NAME, "password" )
    password_element.send_keys("test")
    button_element = driver.find_element(By.ID, "js-login-btn")
    """<button type="submit" 
       id="js-login-btn" 
       class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)" 
       onclick="login.login(event)" 
       data-qa="sibequkica">
	"""
    button_element.click()
    time.sleep(3)
    """<div 
    class="notification-box-description" 
    id="js-notification-box-msg" 
    data-qa="rixawilomi">Your email, password, IP address or location did not match</div>
    """
    error_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description" )
    print(error_web_element)
    assert error_web_element.text == "Your email, password, IP address or location did not match"

    time.sleep(5)
    driver.quit()