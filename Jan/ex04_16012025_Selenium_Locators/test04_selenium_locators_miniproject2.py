import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

@allure.title("Verify clicking start free trial link")
@allure.description("Verify clicking start free trial link and new page url")
@pytest.mark.VWO
def test_app_vwo_free_trial_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))
    """<a 
    href="https://vwo.com/free-trial/?utm_medium=website&amp;
    utm_source=login-page&amp;
    utm_campaign=mof_eg_loginpage" 
    class="text-link" 
    data-qa="bericafeqo">
    Start a free trial
    </a>
    """
    # Link_text --  exact match
    anchar_tag_element = driver.find_element(By.LINK_TEXT, "Start a free trial")
    anchar_tag_element.click()

    # # partial_text --  contains match
    # anchar_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    # anchar_tag_element.click()

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    time.sleep(5)
    driver.quit()