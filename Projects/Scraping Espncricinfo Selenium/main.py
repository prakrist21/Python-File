from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import Players1

team1df=pd.DataFrame(columns=['Bowler','Runs','OverDetail'])
team2df=pd.DataFrame(columns=['Bowler','Runs','OverDetail'])
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
        self.driver.get("https://www.espncricinfo.com/series/new-zealand-vs-pakistan-2024-25-1443540/new-zealand-vs-pakistan-2nd-t20i-1443550/match-overs-comparison")
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(15)
        # self.driver.switch_to.alert.dismiss()
        try:
            self.driver.find_element(By.XPATH,"//button[@id='wzrk-cancel']").click()
        except:
            pass
        time.sleep(2)
        
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

    def matchDetail(self):
        matchdetail=self.driver.find_element(By.XPATH,"//div[@class='ds-text-tight-m ds-font-regular ds-text-typo-mid3']").text
        matchno=matchdetail.split(' ')[0][:-2]
        time.sleep(2)
        return matchno

    def OverData(self):
        bowlers=[]
        runs=[]
        odetail=[]
        self.mains=[]
        bowler=self.driver.find_elements(By.XPATH,"//div[@class='ds-text-compact-xs ds-pt-2 ds-mt-2']")
        run=self.driver.find_elements(By.XPATH,"//span[@class='ds-text-tight-s ds-font-regular ds-ml-1 ds-text-typo-mid2']")
        overdetail=self.driver.find_elements(By.XPATH,"//div[@class='ds-flex ds-my-3 ds--ml-1 ds-flex-wrap']")
        for x in bowler:
            bowlers.append(x.text)
        for y in run:
            runs.append(y.text)
        for m in overdetail:
            d=m.text
            d=d.replace("\n",",")
            d=d.replace("•","0")
            odetail.append(d)
        for z in range(len(runs)):
            self.mains.append([bowlers[z],runs[z],odetail[z]])
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
matchno=c1.matchDetail()
c1.clicking()
c1.OverData()
c1.manageData(list(Players1.b1['Bowling']),list(Players1.b2['Bowling']))
c1.loadDf()
