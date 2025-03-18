import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np
def ScrapeBowlers(tableno):
    df=None
    url="https://www.espncricinfo.com/series/new-zealand-vs-pakistan-2024-25-1443540/new-zealand-vs-pakistan-2nd-t20i-1443550/full-scorecard"
    useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    responce=requests.get(url,headers={'User-Agent':useragent})
    page=BeautifulSoup(responce.text,"html.parser")
    table=page.find_all("table",class_="ds-w-full ds-table ds-table-md ds-table-auto")[tableno]
    head=table.find_all("th")
    header=[x.text.strip() for x in head]
    df=pd.DataFrame(columns=header)
    body=table.find_all('tr')
    for row in body[1:]:
        row_data=row.find_all('td')
        row_data_indi=[x.text.strip() for x in row_data]
        if len(row_data_indi)!=1:
            l=len(df)
            df.loc[l]=row_data_indi
    return df
    

b1=ScrapeBowlers(0)
b2=ScrapeBowlers(1)
print(b1)
print(b2)