

# import requests

import os
# from pandas import pandas
# print(os.environ['PYTHONPATH'].split(os.pathsep))

# from bs4 import BeatifulSoup
from selenium import webdriver
import pandas as pd
# import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://www.ncs.gov.ie/en/childcare-search/")


driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "#ccc-close").click()


selectCounty = Select(driver.find_element(By.CSS_SELECTOR, ".panel-body  #entitylist-filters > li:first-child .form-control"))

selectCounty.select_by_visible_text('Donegal')


driver.find_element(By.CSS_SELECTOR, ".panel-body  #entitylist-filters > li:nth-child(2) .form-control").send_keys("letterkenny" )

driver.find_element(By.CSS_SELECTOR, ".btn-entitylist-filter-submit").click()

driver.implicitly_wait(5)

email_elem = driver.find_elements(By.CSS_SELECTOR, "table tr")


dataToSave = []
df = pd.DataFrame(dataToSave, columns=['School Name', 'Email', 'Phone'])

for email in email_elem:
  school_name = email.find_element(By.CSS_SELECTOR, "td:nth-child(1) a").text
  email_data = eamil.find_element(By.CSS_SELECTOR, "td:nth-child(6) a").text
  phone = eamil.find_element(By.CSS_SELECTOR, "td:nth-child(7) a").text
  dataToSave.append[school_name, email_data, phone]

print(df)

