from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url="https://en.wikipedia.org/wiki/2016_Kolkata_Knight_Riders_season"
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get(url)
driver.maximize_window()

table=driver.find_element(By.XPATH,"//table[@class='wikitable sortable jquery-tablesorter']")
time.sleep(2)

for x in table.find_elements(By.XPATH,"//tr"):
    row=[y.text for y in x.find_elements(By.XPATH,"//td")]
    print(row)