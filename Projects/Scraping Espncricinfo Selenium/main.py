from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

team1df=pd.DataFrame(columns=['Bowler','Runs'])
team2df=pd.DataFrame(columns=['Bowler','Runs'])
class Cricket:
    def __init__(self):
        self.driver=None
        self.mains=None
        self.team1=None
        self.team2=None
    
    def setup(self):
        options=webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        self.driver=webdriver.Chrome(options=options)
        self.driver.get("https://www.espncricinfo.com/series/icc-champions-trophy-2024-25-1459031/india-vs-new-zealand-final-1466428/match-overs-comparison")
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(15)
        # self.driver.switch_to.alert.dismiss()
        try:
            self.driver.find_element(By.XPATH,"//button[@id='wzrk-cancel']").click()
        except:
            pass
        
    def clicking(self):
        option=self.driver.find_elements(By.XPATH,"//td[@class='ds-min-w-max !ds-align-top']")
        option1=self.driver.find_elements(By.XPATH,"//td[@class='ds-min-w-max !ds-align-top ds-bg-ui-fill-translucent']")
        opt=self.driver.find_elements(By.XPATH,"//td[@class='ds-min-w-max ds-cursor-pointer ds-align-top']")
        for y in option1:
            option.append(y)
        time.sleep(2)
        for x in opt[1:]:
            x.click()
        time.sleep(10)

    def OverData(self):
        bowlers=[]
        runs=[]
        self.mains=[]
        bowler=self.driver.find_elements(By.XPATH,"//div[@class='ds-text-compact-xs ds-pt-2 ds-mt-2']")
        run=self.driver.find_elements(By.XPATH,"//span[@class='ds-text-tight-s ds-font-regular ds-ml-1 ds-text-typo-mid2']")
        for x in bowler:
            bowlers.append(x.text)
        for y in run:
            runs.append(y.text)
        for z in range(len(runs)):
            self.mains.append([bowlers[z],runs[z]])
        print(self.mains)
    
    def manageData(self,bowlTeam1,bowlTeam2):
        self.team1=[]
        self.team2=[]
        for x in self.mains:
            x[0]=x[0].replace("Bowler: ","")
            if x[0] in bowlTeam1:
                self.team1.append(x)
            elif x[0] in bowlTeam2:
                self.team2.append(x)

    def loadDf(self):
        for x in self.team1:
            l=len(team1df)
            team1df.loc[l]=x
        for y in self.team2:
            l=len(team2df)
            print(y)
            team2df.loc[l]=y
        
        team1df.to_csv("Team1.csv",index=False)
        team2df.to_csv("Team2.csv",index=False)
        print("Dataframe loaded!!!")
        

        

c1=Cricket()
c1.setup()
c1.clicking()
c1.OverData()
c1.manageData(["Mohammed Shami","Hardik Pandya","Varun Chakravarthy","Kuldeep Yadav","Axar Patel","Ravindra Jadeja"],["Kyle Jamieson","Will O'Rourke","Nathan Smith","Mitchell Santner","Rachin Ravindra","Michael Bracewell","Glenn Phillips"])
c1.loadDf()
