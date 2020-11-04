import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime as dt
import pandas as pd
import datetime
from datetime import date
import openpyxl
from collections import OrderedDict
import pyexcel
import xlrd
from xlrd import open_workbook
from heapq import merge 
import os
import requests
import urllib.request, json 
import yfinance as yf
import pandas_datareader as pdr


cwd = os.getcwd()
date_month=date.today()
date_today=date.today()-datetime.timedelta(50)


##############################################################################MVDA###########################################################################################################################################################
with urllib.request.urlopen("https://min-api.cryptocompare.com/data/index/histo/day?indexName=MVDA&limit=50&api_key=599a7777686b216e65e259ad35301659aae87d7f7d5a94cd43a791aac8d3d066") as url:
    data = json.loads(url.read().decode())
    

data_mvda=[]
for i in range(0,49):
	time=data["Data"][i]['time']
	ts = int(time)
	time=dt.datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y')
	value=data["Data"][i]['close']
	data_mvda.append([time,value])
print(data_mvda)
df=pd.DataFrame(data_mvda,columns=['DATE','MVDA'])

df.to_csv(cwd+"/FINAL/IGNORE/MVDA_MVIS_FINAL.csv",index=False,header=True,index_label="DATE")


x3 = pd.read_csv(cwd+"/BASE/MVDA_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/MVDA_MVIS_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


mvda_final_hope_2=pd.concat([x3,x4]).reset_index()#.drop_duplicates(keep="last")
df4=pd.DataFrame(mvda_final_hope_2)
df4 = df4.dropna()
df4=df4.set_index("DATE")
df_ma2= df4[~df4.index.duplicated()]

df_ma2.to_csv(cwd+"/FINAL/MVDA_FINAL.csv",index=True,index_label="DATE")
df_ma2.to_csv(cwd+"/BASE/MVDA_BASE.csv",index=True,index_label="DATE")


################################################################MVDALC####################################################################
with urllib.request.urlopen("https://min-api.cryptocompare.com/data/index/histo/day?indexName=MVDALC&limit=50&api_key=599a7777686b216e65e259ad35301659aae87d7f7d5a94cd43a791aac8d3d066") as url:
    data = json.loads(url.read().decode())
    

data_mvdalc=[]
for i in range(0,49):
	time=data["Data"][i]['time']
	ts = int(time)
	time=dt.datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y')
	value=data["Data"][i]['close']
	data_mvdalc.append([time,value])

df=pd.DataFrame(data_mvdalc,columns=['DATE','MVDALC'])

df.to_csv(cwd+"/FINAL/IGNORE/MVDALC_MVIS_FINAL.csv",index=False,header=True,index_label="DATE")


x3 = pd.read_csv(cwd+"/BASE/MVDALC_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/MVDALC_MVIS_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


mvdalc_final_hope_2=pd.concat([x3,x4]).reset_index()#.drop_duplicates(keep="last")
df4=pd.DataFrame(mvdalc_final_hope_2)
df4 = df4.dropna()
df4=df4.set_index("DATE")
df_malc2= df4[~df4.index.duplicated()]


df_malc2.to_csv(cwd+"/FINAL/MVDALC_FINAL.csv",index=True,index_label="DATE")
df_malc2.to_csv(cwd+"/BASE/MVDALC_BASE.csv",index=True,index_label="DATE")



##########################################################MVDAMC###############################################################################

with urllib.request.urlopen("https://min-api.cryptocompare.com/data/index/histo/day?indexName=MVDAMC&limit=50&api_key=599a7777686b216e65e259ad35301659aae87d7f7d5a94cd43a791aac8d3d066") as url:
    data = json.loads(url.read().decode())
    

data_mvdamc=[]
for i in range(0,49):
	time=data["Data"][i]['time']
	ts = int(time)
	time=dt.datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y')
	value=data["Data"][i]['close']
	data_mvdamc.append([time,value])

df=pd.DataFrame(data_mvdamc,columns=['DATE','MVDAMC'])
df.to_csv(cwd+"/FINAL/IGNORE/MVDAMC_MVIS_FINAL.csv",index=False,header=True,index_label="DATE")


x3 = pd.read_csv(cwd+"/BASE/MVDAMC_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/MVDAMC_MVIS_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


mvdamc_final_hope_2=pd.concat([x3,x4]).reset_index()#.drop_duplicates(keep="last")
df4=pd.DataFrame(mvdamc_final_hope_2)
df4 = df4.dropna()
df4=df4.set_index("DATE")

df_mamc2= df4[~df4.index.duplicated()]

df_mamc2.to_csv(cwd+"/FINAL/MVDAMC_FINAL.csv",index=True,index_label="DATE")
df_mamc2.to_csv(cwd+"/BASE/MVDAMC_BASE.csv",index=True,index_label="DATE")


#########################################################################################MVDASC#####################################################################

with urllib.request.urlopen("https://min-api.cryptocompare.com/data/index/histo/day?indexName=MVDASC&limit=50&api_key=599a7777686b216e65e259ad35301659aae87d7f7d5a94cd43a791aac8d3d066") as url:
    data = json.loads(url.read().decode())
    

data_mvdasc=[]
for i in range(0,49):
	time=data["Data"][i]['time']
	ts = int(time)
	time=dt.datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y')
	value=data["Data"][i]['close']
	data_mvdasc.append([time,value])

df=pd.DataFrame(data_mvdasc,columns=['DATE','MVDASC'])
df.to_csv(cwd+"/FINAL/IGNORE/MVDASC_MVIS_FINAL.csv",index=False,header=True,index_label="DATE")


x3 = pd.read_csv(cwd+"/BASE/MVDASC_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/MVDASC_MVIS_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


mvdasc_final_hope_2=pd.concat([x3,x4]).reset_index()#.drop_duplicates(keep="last")
df4=pd.DataFrame(mvdasc_final_hope_2)
df4 = df4.dropna()
df4=df4.set_index("DATE")

df_masc2= df4[~df4.index.duplicated()]

df_masc2.to_csv(cwd+"/FINAL/MVDASC_FINAL.csv",index=True,index_label="DATE")
df_masc2.to_csv(cwd+"/BASE/MVDASC_BASE.csv",index=True,index_label="DATE")




#####################################################################################VGTSX######################################################################



VGTSX=yf.Ticker("VT")
VGTSX_hist=VGTSX.history(period="50d")

df=pd.DataFrame(VGTSX_hist["Close"])
df.columns=['VGTSX']

print(df.head(30))
df = df.resample('D').asfreq()

df= df.interpolate(method='linear', axis=0).ffill().bfill()

df.to_csv(cwd+"/FINAL/IGNORE/VGTSX_YAHOO_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/VGTSX_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/VGTSX_YAHOO_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


vgtsx_final_hope_2=pd.concat([x3,x4]).reset_index() #.drop_duplicates(keep="last")
df4=pd.DataFrame(vgtsx_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))
df4= df4.set_index('DATE') 


df_vg2 = df4[~df4.index.duplicated()]

df_vg2.to_csv(cwd+"/FINAL/VGTSX_FINAL.csv",index=True,index_label="DATE")
df_vg2.to_csv(cwd+"/BASE/VGTSX_BASE.csv",index=True,index_label="DATE")





###############################################################################CORP########################################################################

r = requests.get('https://ts-api.cnbc.com/harmony/app/bars/CORP-GB/1D/20190121000000/20201126000000/adjusted/EST5EDT.json')
r=r.json()
CORP_DATA={}

for i in range(0,len(r['barData']['priceBars'])):

	date_2=(r['barData']['priceBars'][i]['tradeTime'])
	value=(r['barData']['priceBars'][i]['close'])
	CORP_DATA[date_2]=value



df1=pd.DataFrame.from_dict(CORP_DATA,orient="index",columns=["CORP"])



df1.index.names = ['DATE']
df1.index= pd.to_datetime(df1.index)

df1 = df1.resample('D').asfreq()
df1["CORP"] = pd.to_numeric(df1["CORP"], errors='coerce')
df1= df1.interpolate(method='linear', axis=0).ffill().bfill()

df1.to_csv(cwd+"/FINAL/IGNORE/CORP_CNBC_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/CORP_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/CORP_CNBC_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


corp_final_hope_2=pd.concat([x3,x4]).reset_index() #.drop_duplicates(keep="last")
df4=pd.DataFrame(corp_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4= df4.set_index('DATE') 
df_cp2 = df4[~df4.index.duplicated()]

df_cp2.to_csv(cwd+"/FINAL/CORP_FINAL.csv",index=True,index_label="DATE")
df_cp2.to_csv(cwd+"/BASE/CORP_BASE.csv",index=True,index_label="DATE")


#################################################################SPGSCITR################################################################################

url = "https://rapidapi.p.rapidapi.com/market/get-chart"

querystring = {"interval":"m3","id":"SPGSCITR:IND"}

headers = {
    'x-rapidapi-key': "dd4e4d0869msh30007d9d5e5d0abp133b50jsn1247da1d4fa9",
    'x-rapidapi-host': "bloomberg-market-and-financial-news.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

spgscitr_bl=response.json()

spgscitr_bl_data=[]
for i in range(0,65):
	date_1=spgscitr_bl['result']["SPGSCITR:IND"]["ticks"][i]['time']
	date_1=datetime.datetime.fromtimestamp(date_1)
	date_2=date_1.strftime('%Y %m %d')
	value=spgscitr_bl['result']["SPGSCITR:IND"]["ticks"][i]['close']
	spgscitr_bl_data.append([date_2,value])

df1=pd.DataFrame(spgscitr_bl_data)

df1.columns=['DATE','SPGSCITR']
df1.set_index("DATE",inplace=True)

#df1.index.names = ['DATE']
df1.index= pd.to_datetime(df1.index)

df1 = df1.resample('D').asfreq()
print(df1)
df1= df1.interpolate(method='linear', axis=0).ffill().bfill()

df1.to_csv(cwd+"/FINAL/IGNORE/SPGSCITR_BLOOMBERG_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/SPGSCITR_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/SPGSCITR_BLOOMBERG_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


spgscitr_final_hope_2=pd.concat([x3,x4]).reset_index() #.drop_duplicates(keep="last")
df4=pd.DataFrame(spgscitr_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4= df4.set_index('DATE') 
df_spg2 = df4[~df4.index.duplicated()]

df_spg2.to_csv(cwd+"/FINAL/SPGSCITR_FINAL.csv",index=True,index_label="DATE")
df_spg2.to_csv(cwd+"/BASE/SPGSCITR_BASE.csv",index=True,index_label="DATE")


##################################################REET###########################################################################################



REET=yf.Ticker("REET")
REET_hist=REET.history(period="50d")

df=pd.DataFrame(REET_hist["Close"])
df.columns=['REET']

df = df.resample('D').asfreq()

df= df.interpolate(method='linear', axis=0).ffill().bfill()
df.to_csv(cwd+"/FINAL/IGNORE/REET_YAHOO_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/REET_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/REET_YAHOO_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


reet_final_hope_2=pd.concat([x3,x4]).reset_index() #.drop_duplicates(keep="last")
df4=pd.DataFrame(reet_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))
df4= df4.set_index('DATE') 

df_rt2 = df4[~df4.index.duplicated()]

df_rt2.to_csv(cwd+"/FINAL/REET_FINAL.csv",index=True,index_label="DATE")
df_rt2.to_csv(cwd+"/BASE/REET_BASE.csv",index=True,index_label="DATE")


##################################DTWEXBGS###########################################################################


start_date = date.today()-datetime.timedelta(100)
end_date = date.today()
fx = pdr.get_data_fred("DTWEXBGS", start_date, end_date)

df=pd.DataFrame(fx)
df.columns=['DTWEXBGS']
print(df)
df = df.resample('D').asfreq()
df= df.interpolate(method='linear', axis=0).ffill().bfill()
df.to_csv(cwd+"/FINAL/IGNORE/DTWEXBGS_FRED_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/DTWEXBGS_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/DTWEXBGS_FRED_FINAL.csv",parse_dates=["DATE"], dayfirst=True,index_col="DATE")

ust_final_hope_2=pd.concat([x3,x4]).reset_index() #.drop_duplicates(keep="first")
df4=pd.DataFrame(ust_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))
df4= df4.set_index('DATE') 
df_ds2 = df4[~df4.index.duplicated()]

df_ds2.to_csv(cwd+"/FINAL/DTWEXBGS_FINAL.csv",index=True,index_label="DATE")
df_ds2.to_csv(cwd+"/BASE/DTWEXBGS_BASE.csv",index=True,index_label="DATE")




###############################################################GOLD######################################################################



start_date = date.today()-datetime.timedelta(100)
end_date = date.today()
fx = pdr.get_data_fred("GOLDPMGBD228NLBM", start_date, end_date)

df=pd.DataFrame(fx)
df.columns=['GOLD SPOT']
print(df)
df = df.resample('D').asfreq()
df= df.interpolate(method='linear', axis=0).ffill().bfill()
df.to_csv(cwd+"/FINAL/IGNORE/GOLD_FRED_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/GOLD_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/GOLD_FRED_FINAL.csv",parse_dates=["DATE"], dayfirst=True,index_col="DATE")

gold_final_hope_2=pd.concat([x3,x4]).reset_index() #.drop_duplicates(keep="first")
df4=pd.DataFrame(gold_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))
df4= df4.set_index('DATE') 

df_gd2 = df4[~df4.index.duplicated()]

df_gd2.to_csv(cwd+"/FINAL/GOLD_FINAL.csv",index=True,index_label="DATE")
df_gd2.to_csv(cwd+"/BASE/GOLD_BASE.csv",index=True,index_label="DATE")









###############################################################VIX############################################################################

start_date = date.today()-datetime.timedelta(100)
end_date = date.today()
fx = pdr.get_data_fred("VIXCLS", start_date, end_date)

df=pd.DataFrame(fx)
df.columns=['VIX']
print(df)
df = df.resample('D').asfreq()
df= df.interpolate(method='linear', axis=0).ffill().bfill()
df.to_csv(cwd+"/FINAL/IGNORE/VIX_FRED_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/VIX_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/VIX_FRED_FINAL.csv",parse_dates=["DATE"], dayfirst=True,index_col="DATE")

vix_final_hope_2=pd.concat([x3,x4]).reset_index() #.drop_duplicates(keep="first")
df4=pd.DataFrame(vix_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4=df4.set_index("DATE")
df_vx2= df4[~df4.index.duplicated()]
df_vx2.to_csv(cwd+"/FINAL/VIX_FINAL.csv",index=True,index_label="DATE")
df_vx2.to_csv(cwd+"/BASE/VIX_BASE.csv",index=True,index_label="DATE")





##########################################################################USTs#########################################################################

start_date = date.today()-datetime.timedelta(100)
end_date = date.today()
fx = pdr.get_data_fred("DGS10", start_date, end_date)

df=pd.DataFrame(fx)
df.columns=['UST']
df = df.resample('D').asfreq()
df= df.interpolate(method='linear', axis=0).ffill().bfill()
df.to_csv(cwd+"/FINAL/IGNORE/UST_FRED_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/UST_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/UST_FRED_FINAL.csv",parse_dates=["DATE"], dayfirst=True,index_col="DATE")

ust_final_hope_2=pd.concat([x3,x4]).reset_index() #.drop_duplicates(keep="first")
df4=pd.DataFrame(ust_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))
df4=df4.set_index("DATE")
df_ut2 = df4[~df4.index.duplicated()]
df_ut2.to_csv(cwd+"/FINAL/UST_FINAL.csv",index=True,index_label="DATE")
df_ut2.to_csv(cwd+"/BASE/UST_BASE.csv",index=True,index_label="DATE")





##########################################################################SP500#####################################################################

start_date = date.today()-datetime.timedelta(100)
end_date = date.today()
fx = pdr.get_data_fred("SP500", start_date, end_date)

df=pd.DataFrame(fx)
df.columns=['SP500']
print(df)
df = df.resample('D').asfreq()
df= df.interpolate(method='linear', axis=0).ffill().bfill()
df.to_csv(cwd+"/FINAL/IGNORE/SP500_FRED_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/SP500_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/SP500_FRED_FINAL.csv",parse_dates=["DATE"], dayfirst=True,index_col="DATE")

sp500_final_hope_2=pd.concat([x3,x4]).reset_index() #.drop_duplicates(keep="first")
df4=pd.DataFrame(sp500_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4=df4.set_index("DATE")
df_sp2 = df4[~df4.index.duplicated()]

df_sp2.to_csv(cwd+"/FINAL/SP500_FINAL.csv",index=True,index_label="DATE")
df_sp2.to_csv(cwd+"/BASE/SP500_BASE.csv",index=True,index_label="DATE")





###########################################################################CCBTC##################################################################

with urllib.request.urlopen("https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=50") as url:
    data = json.loads(url.read().decode())
    


#print(data["Data"]["Data"][0])


data_ccbtc=[]
for i in range(0,49):
	time=data["Data"]["Data"][i]['time']
	ts = int(time)
	time=dt.datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y')
	close_v=data["Data"]["Data"][i]['close']
	open_v=data["Data"]["Data"][i]['open']
	data_ccbtc.append([time,close_v,open_v])

df=pd.DataFrame(data_ccbtc,columns=['DATE','CCBTC_CLOSE',"CCBTC_OPEN"])

df.to_csv(cwd+"/FINAL/IGNORE/CCBTC_CC_FINAL.csv",index=False,header=True,index_label="DATE")


x3 = pd.read_csv(cwd+"/BASE/CCBTC_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/CCBTC_CC_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


ccbtc_final_hope_2=pd.concat([x3,x4]).drop_duplicates(keep="last").reset_index()
df4=pd.DataFrame(ccbtc_final_hope_2)
df4 = df4.dropna()
df4=df4.set_index("DATE")
df_cc2 = df4[~df4.index.duplicated()]

df_cc2.to_csv(cwd+"/FINAL/CCBTC_FINAL.csv",index=True,index_label="DATE")
df_cc2.to_csv(cwd+"/BASE/CCBTC_BASE.csv",index=True,index_label="DATE")




################################################################################COMBINED_EXCEL######################################################

new = pd.concat([df_ma2,df_malc2,df_mamc2,df_masc2,df_vg2,df_cp2,df_spg2,df_rt2,df_ds2,df_gd2,df_vx2,df_ut2,df_sp2,df_cc2], axis=1) 
new.to_csv(cwd+"/COMBINED/RAW_DATA.csv")


















