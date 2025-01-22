from selenium import webdriver
from selenium.webdriver.common.by import By

# finding all the elements in dynamic web table
def test_web_tables_dynamic():
    driver = webdriver.Firefox()
    driver.get("https://awesomeqa.com/webtable1.html")
    # driver.maximize_window()
    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")
    row_table = table.find_elements(By.TAG_NAME, "tr")

    for row in row_table:
        cols = row.find_elements(By.TAG_NAME, "td")
        for e in cols:
            print(e.text)

    driver.quit()
