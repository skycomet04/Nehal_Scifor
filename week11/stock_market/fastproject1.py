from fastapi import FastAPI #importing fastapi as an object
from typing import Optional
import requests

app=FastAPI()# creating the instance of fastapi

@app.get("/display/{symbol}/")
async def stock_data(symbol:str):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=520WMU68NTAWP0UG"
    url1=f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey=520WMU68NTAWP0UG"
    res = requests.get(url)
    data=res.json()
    price= data['Global Quote']['05. price']
    print(data)
    res1=requests.get(url1)
    data1=res1.json()
    print(data1)
    desc=data1['Description']
    return {'Price':price,'Description':desc}
@app.get("/historical_data/{symbol}/")
async def historic_data(symbol:str):
    url = f"https://yahoo-finance127.p.rapidapi.com/historic/{symbol}/1d/1mo"

    headers = {
        "X-RapidAPI-Key": "11a9317e4bmsh45d55b906008e11p158722jsnd5086ba06d52",
        "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    stock=response.json()
    all_data=stock['indicators']['quote'][0]
    return {'Hitorical data':all_data}
