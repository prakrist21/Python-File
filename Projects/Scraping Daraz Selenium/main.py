# Scraping Mobile phones in daraz website. [Only pages 1-3]
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

df=pd.DataFrame(columns=['Name','Price'])
class Daraz:
    global df
    mainlst=[]
    def __init__(self):
        self.driver=None
        self.url="https://www.daraz.com.np/catalog/?page=1&q=laptop"
    
    def setup(self):
        options=webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(options=options)
        self.driver.get(self.url)
        self.driver.maximize_window()

    def getValues(self):
        name=self.driver.find_elements(By.XPATH,"//div[@class='RfADt']")
        price=self.driver.find_elements(By.XPATH,"//div[@class='aBrP0']")
        names=[]
        prices=[]
        for x in name:
            names.append(x.text)
        for y in price:
            prices.append(y.text)

        for x in range(len(prices)):
            short_lst=[names[x],prices[x]]
            self.mainlst.append(short_lst)
            short_lst=[]

    def loadDf(self):
        print(self.mainlst)
        for x in self.mainlst:
            l=len(df)
            df.loc[l]=x
        self.mainlst=[]

    def nextPage(self):
        old_url=self.driver.current_url
        self.driver.execute_script('window.scrollBy(0,4350);')
        self.driver.find_element(By.XPATH,"//li[@title='Next Page']").click()
        new_url=self.driver.current_url
        if old_url==new_url:
            df.to_csv("New.csv",index=False)
            quit()
        # Adjust page number accordingly 
        elif "page=20" in new_url:
            df.to_csv("New.csv",index=False)
            quit()
        self.url=new_url    
        time.sleep(3)

w1=Daraz()
w1.setup()
while True:
    w1.getValues()
    w1.loadDf()
    w1.nextPage()
    if 1==0:
        break

