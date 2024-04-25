import numpy
import pandas as p
import matplotlib.pyplot as pp
import seaborn as sn
data=p.read_csv("C:/Users/ishan/OneDrive/Desktop/python/nasa/lunar.csv")
print(data.shape)
null_col=data.isnull().sum()
print(data.info())
#print(f"Lunar Catalog with maximum eclipse time {data.loc[],'Catalog Number'}")
calendar=data["Calendar Date"].str.split(" ",expand=True)
data['Year']=calendar[0]
data['month']=calendar[1]
data['date']=calendar[2]
data.rename(columns={'Partial Eclipse Duration (m)':'PartialEclipseDur'},inplace=True)
max_no=data.loc[data['Year']=='1995','Eclipse Time'].max()
print(max_no)
print(data['Eclipse Time'].min())
yeargroup=data.groupby('Year')['PartialEclipseDur'].count()


 
