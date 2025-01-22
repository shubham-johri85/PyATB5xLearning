from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web_tables():
    driver = webdriver.Firefox()
    driver.get("https://awesomeqa.com/webtable.html")
    # driver.maximize_window()
    row_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")
    rows = len(row_elements)
    print("Number of rows are-->", rows)
    col_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[2]/td")
    cols = len(col_elements)
    print("Number of cols are-->", cols)
    contact_name = driver.find_element(By.XPATH, "//table[@id='customers']/tbody/tr[4]/td[2]")
    name = contact_name.text
    print("The name in table is-->", name)
    country = driver.find_element(By.XPATH, "//table[@id='customers']/tbody/tr[4]/td[2]/following-sibling::td")
    comntry_name = country.text
    print("The country is-->", comntry_name)
    company = driver.find_element(By.XPATH, "//table[@id='customers']/tbody/tr[4]/td[2]/preceding-sibling::td")
    company_name = company.text
    print("He is from-->", company_name)
    driver.quit()
