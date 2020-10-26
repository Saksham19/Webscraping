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



#setting up webdrive

#PATH = "C:\Program Files (x86)\chromedriver.exe"
#driver = webdriver.Chrome(PATH)

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

df=pd.DataFrame(data_mvda,columns=['DATE','MVDA'])

df.to_csv(cwd+"/FINAL/IGNORE/MVDA_MVIS_FINAL.csv",index=False,header=True,index_label="DATE")


x3 = pd.read_csv(cwd+"/BASE/MVDA_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/MVDA_MVIS_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


mvda_final_hope_2=pd.concat([x3,x4]).drop_duplicates(keep="last").reset_index()
df4=pd.DataFrame(mvda_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4.to_csv(cwd+"/FINAL/IGNORE/MVDA_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_ma = pd.read_csv(cwd+"/FINAL/IGNORE/MVDA_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
df_ma.drop_duplicates(inplace=True)
df_ma.to_csv(cwd+"/FINAL/MVDA_FINAL.csv")
df_ma.to_csv(cwd+"/BASE/MVDA_BASE.csv")

df_ma = pd.read_csv(cwd+"/FINAL/MVDA_FINAL.csv")
df_ma['DATE'] = pd.to_datetime(df_ma['DATE'])
df_ma= df_ma.set_index('DATE') 
df_ma2=df_ma.drop_duplicates(inplace=False)
df_ma2 = df_ma2[~df_ma2.index.duplicated()]
df_ma2 = df_ma2.resample('D').asfreq()
df_ma2= df_ma2.interpolate(method='linear', axis=0).ffill().bfill()


df_ma2.to_csv(cwd+"/FINAL/MVDA_FINAL.csv")
df_ma2.to_csv(cwd+"/BASE/MVDA_BASE.csv")


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


mvdalc_final_hope_2=pd.concat([x3,x4]).drop_duplicates(keep="last").reset_index()
df4=pd.DataFrame(mvdalc_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4.to_csv(cwd+"/FINAL/IGNORE/MVDALC_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_malc = pd.read_csv(cwd+"/FINAL/IGNORE/MVDALC_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
df_malc.drop_duplicates(inplace=True)
df_malc.to_csv(cwd+"/FINAL/MVDALC_FINAL.csv")
df_malc.to_csv(cwd+"/BASE/MVDALC_BASE.csv")

df_malc = pd.read_csv(cwd+"/FINAL/MVDALC_FINAL.csv")
df_malc['DATE'] = pd.to_datetime(df_malc['DATE'])
df_malc= df_malc.set_index('DATE') 
df_malc2=df_malc.drop_duplicates(inplace=False)
df_malc2 = df_malc2[~df_malc2.index.duplicated()]

df_malc2 = df_malc2.resample('D').asfreq()
df_malc2= df_malc2.interpolate(method='linear', axis=0).ffill().bfill()

df_malc2.to_csv(cwd+"/FINAL/MVDALC_FINAL.csv")
df_malc2.to_csv(cwd+"/BASE/MVDALC_BASE.csv")




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


mvdamc_final_hope_2=pd.concat([x3,x4]).drop_duplicates(keep="last").reset_index()
df4=pd.DataFrame(mvdamc_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4.to_csv(cwd+"/FINAL/IGNORE/MVDAMC_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_mamc = pd.read_csv(cwd+"/FINAL/IGNORE/MVDAMC_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
df_mamc.drop_duplicates(inplace=True)
df_mamc.to_csv(cwd+"/FINAL/MVDAMC_FINAL.csv")
df_mamc.to_csv(cwd+"/BASE/MVDAMC_BASE.csv")

df_mamc = pd.read_csv(cwd+"/FINAL/MVDAMC_FINAL.csv")
df_mamc['DATE'] = pd.to_datetime(df_mamc['DATE'])
df_mamc= df_mamc.set_index('DATE') 
df_mamc2=df_mamc.drop_duplicates(inplace=False)
df_mamc2 = df_mamc2[~df_mamc2.index.duplicated()]

df_mamc2 = df_mamc2.resample('D').asfreq()
df_mamc2= df_mamc2.interpolate(method='linear', axis=0).ffill().bfill()

df_mamc2.to_csv(cwd+"/FINAL/MVDAMC_FINAL.csv")
df_mamc2.to_csv(cwd+"/BASE/MVDAMC_BASE.csv")


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


mvdasc_final_hope_2=pd.concat([x3,x4]).drop_duplicates(keep="last").reset_index()
df4=pd.DataFrame(mvdasc_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4.to_csv(cwd+"/FINAL/IGNORE/MVDASC_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_masc = pd.read_csv(cwd+"/FINAL/IGNORE/MVDASC_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
df_masc.drop_duplicates(inplace=True)
df_masc.to_csv(cwd+"/FINAL/MVDASC_FINAL.csv")
df_masc.to_csv(cwd+"/BASE/MVDASC_BASE.csv")

df_masc = pd.read_csv(cwd+"/FINAL/MVDASC_FINAL.csv")
df_masc['DATE'] = pd.to_datetime(df_masc['DATE'])
df_masc= df_masc.set_index('DATE') 
df_masc2=df_masc.drop_duplicates(inplace=False)
df_masc2 = df_masc2[~df_masc2.index.duplicated()]

df_masc2 = df_masc2.resample('D').asfreq()
df_masc2= df_masc2.interpolate(method='linear', axis=0).ffill().bfill()


df_masc2.to_csv(cwd+"/FINAL/MVDASC_FINAL.csv")
df_masc2.to_csv(cwd+"/BASE/MVDASC_BASE.csv")







#####################################################################################VGTSX######################################################################


VGTSX=yf.Ticker("VT")
VGTSX_hist=VGTSX.history(period="50d")

df=pd.DataFrame(VGTSX_hist["Close"])
df.columns=['VGTSX']
df.to_csv(cwd+"/FINAL/IGNORE/VGTSX_YAHOO_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/VGTSX_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/VGTSX_YAHOO_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


vgtsx_final_hope_2=pd.concat([x3,x4]).drop_duplicates(keep="last").reset_index()
df4=pd.DataFrame(vgtsx_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4.to_csv(cwd+"/FINAL/IGNORE/VGTSX_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_vg = pd.read_csv(cwd+"/FINAL/IGNORE/VGTSX_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
df_vg.drop_duplicates(inplace=True)
df_vg.to_csv(cwd+"/FINAL/VGTSX_FINAL.csv")
df_vg.to_csv(cwd+"/BASE/VGTSX_BASE.csv")

df_vg = pd.read_csv(cwd+"/FINAL/VGTSX_FINAL.csv")
df_vg['DATE'] = pd.to_datetime(df_vg['DATE'])
df_vg= df_vg.set_index('DATE') 
df_vg2=df_vg.drop_duplicates(inplace=False)

df_vg2 = df_vg2[~df_vg2.index.duplicated()]


df_vg2 = df_vg2.resample('D').asfreq()

df_vg2= df_vg2.interpolate(method='linear', axis=0).ffill().bfill()

df_vg2.to_csv(cwd+"/FINAL/VGTSX_FINAL.csv")
df_vg2.to_csv(cwd+"/BASE/VGTSX_BASE.csv")



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
df1.index = pd.to_datetime(df1.index)

df1.to_csv(cwd+"/FINAL/IGNORE/CORP_CNBC_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/CORP_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/CORP_CNBC_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


corp_final_hope_2=pd.concat([x3,x4]).drop_duplicates(keep="last").reset_index()
df4=pd.DataFrame(corp_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4.to_csv(cwd+"/FINAL/IGNORE/CORP_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_cp = pd.read_csv(cwd+"/FINAL/IGNORE/CORP_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
df_cp.drop_duplicates(inplace=True)
df_cp.to_csv(cwd+"/FINAL/CORP_FINAL.csv")
df_cp.to_csv(cwd+"/BASE/CORP_BASE.csv")

df_cp = pd.read_csv(cwd+"/FINAL/CORP_FINAL.csv")
df_cp['DATE'] = pd.to_datetime(df_cp['DATE'])
df_cp= df_cp.set_index('DATE') 
df_cp2=df_cp.drop_duplicates(inplace=False)
df_cp2 = df_cp2[~df_cp2.index.duplicated()]

df_cp2 = df_cp2.resample('D').asfreq()

df_cp2= df_cp2.interpolate(method='linear', axis=0).ffill().bfill()

df_cp2.to_csv(cwd+"/FINAL/CORP_FINAL.csv")
df_cp2.to_csv(cwd+"/BASE/CORP_BASE.csv")



#################################################################SPGSCITR################################################################################

driver = webdriver.Chrome()

dt_string = date_today.strftime("%d/%m/%Y")

my_url="https://seekingalpha.com/symbol/SPGSCITR/historical-price-quotes"
driver.get(my_url)
driver.maximize_window()
driver.minimize_window()

#initializing the action object
action = webdriver.ActionChains(driver)

#calculating the number of rows and columns

rows=len(driver.find_elements_by_xpath("/html/body/div[3]/div[1]/div/div/div/div/div[2]/div/div/div[2]/table/tbody/tr"))

print(rows)

columns=len(driver.find_elements_by_xpath('/html/body/div[3]/div[1]/div/div/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td'))
print(columns)


row_1=driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]").text
print(row_1)

col_1=driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[5]").text

print(col_1)


#for loop for incrementing the no. of rows
SPGSCITR_DATA={}
for r in range(1,51):
	date_2=driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div/div/div[2]/div/div/div[2]/table/tbody/tr["+str(r)+"]/td[1]").text #/html/body/div[3]/div[4]/table/tbody/tr["+str(r)+"]/th
	value=driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div/div/div[2]/div/div/div[2]/table/tbody/tr["+str(r)+"]/td[4]").text
	#SPGSCITR_DATA.append([date_2,value])	
	SPGSCITR_DATA[date_2]=value


driver.quit()
#SPGSCITR_DATA.reverse()	
df=pd.DataFrame.from_dict(SPGSCITR_DATA,orient="index",columns=['SPGSCITR'])['SPGSCITR'].str.replace(",","").iloc[::-1]
df.index.names = ['DATE']
#df=pd.DataFrame(SPGSCITR_DATA,dtype='float32')
#df.columns=['DATE','SPGSCITR']
df.index= pd.to_datetime(df.index)
print(df)
df.to_csv(cwd+"/FINAL/IGNORE/SPGSCITR_REUTERS_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/SPGSCITR_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/SPGSCITR_REUTERS_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


spgscitr_final_hope_2=pd.concat([x3,x4]).drop_duplicates(keep="last").reset_index()
df4=pd.DataFrame(spgscitr_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))
df4.to_csv(cwd+"/FINAL/IGNORE/SPGSCITR_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_sp = pd.read_csv(cwd+"/FINAL/IGNORE/SPGSCITR_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
df_sp.drop_duplicates(inplace=True)
df_sp.to_csv(cwd+"/FINAL/SPGSCITR_FINAL.csv")
df_sp.to_csv(cwd+"/BASE/SPGSCITR_BASE.csv")

df_sp = pd.read_csv(cwd+"/FINAL/SPGSCITR_FINAL.csv")
df_sp['DATE'] = pd.to_datetime(df_sp['DATE'])
df_sp= df_sp.set_index('DATE') 
df_sp2=df_sp.drop_duplicates(inplace=False)
df_sp2 = df_sp2[~df_sp2.index.duplicated()]

df_sp2 = df_sp2.resample('D').asfreq()


df_sp2= df_sp2.interpolate(method='linear', axis=0).ffill().bfill()

df_sp2.to_csv(cwd+"/FINAL/SPGSCITR_FINAL.csv")
df_sp2.to_csv(cwd+"/BASE/SPGSCITR_BASE.csv")


##################################################REET###########################################################################################



REET=yf.Ticker("REET")
REET_hist=REET.history(period="50d")

df=pd.DataFrame(REET_hist["Close"])
df.columns=['REET']
df.to_csv(cwd+"/FINAL/IGNORE/REET_YAHOO_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/REET_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/REET_YAHOO_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


reet_final_hope_2=pd.concat([x3,x4]).drop_duplicates(keep="last").reset_index()
df4=pd.DataFrame(reet_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4.to_csv(cwd+"/FINAL/IGNORE/REET_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_rt = pd.read_csv(cwd+"/FINAL/IGNORE/REET_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
df_rt.drop_duplicates(inplace=True)
df_rt.to_csv(cwd+"/FINAL/REET_FINAL.csv")
df_rt.to_csv(cwd+"/BASE/REET_BASE.csv")

df_rt = pd.read_csv(cwd+"/FINAL/REET_FINAL.csv")
df_rt['DATE'] = pd.to_datetime(df_rt['DATE'])
df_rt= df_rt.set_index('DATE') 
df_rt2=df_rt.drop_duplicates(inplace=False)

df_rt2 = df_rt2[~df_rt2.index.duplicated()]

df_rt2 = df_rt2.resample('D').asfreq()

df_rt2= df_rt2.interpolate(method='linear', axis=0).ffill().bfill()

df_rt2.to_csv(cwd+"/FINAL/REET_FINAL.csv")
df_rt2.to_csv(cwd+"/BASE/REET_BASE.csv")


##################################DTWEXBGS###########################################################################


driver = webdriver.Chrome()

dt_string = date_today.strftime("%d/%m/%Y")

my_url="https://www.federalreserve.gov/releases/h10/summary/jrxwtfb_nb.htm"
driver.get(my_url)
driver.maximize_window()
driver.minimize_window()

#initializing the action object
action = webdriver.ActionChains(driver)

#calculating the number of rows and columns

rows=len(driver.find_elements_by_xpath("/html/body/div[3]/div[4]/table/tbody/tr"))

print(rows)

columns=len(driver.find_elements_by_xpath('/html/body/div[3]/div[4]/table/tbody/tr[1]/td'))
print(columns)


#row_1=driver.find_element_by_xpath("/html/body/div[3]/div[4]/table/tbody/tr[3]/th").text
#print(row_1)

#col_1=driver.find_element_by_xpath("/html/body/div[3]/div[4]/table/tbody/tr[3]/td").text

#print(col_1)

#for loop for incrementing the no. of rows
DTWEXBGS_DATA={}
for r in range(rows-50,rows+1):
	date_2=driver.find_element_by_xpath("/html/body/div[3]/div[4]/table/tbody/tr["+str(r)+"]/th").text
	value=driver.find_element_by_xpath("/html/body/div[3]/div[4]/table/tbody/tr["+str(r)+"]/td").text
	DTWEXBGS_DATA[date_2]=value


driver.quit()
#SPGSCITR_DATA.reverse()	
df=pd.DataFrame.from_dict(DTWEXBGS_DATA,orient="index",columns=['DTWEXBGS'])
df.index.names = ['DATE']
df.index= pd.to_datetime(df.index)
print(df)
df.to_csv(cwd+"/FINAL/IGNORE/DTWEXBGS_FRED_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/DTWEXBGS_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/DTWEXBGS_FRED_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


dtwexbgs_final_hope_2=pd.concat([x3,x4]).drop_duplicates(keep="last").reset_index()
df4=pd.DataFrame(dtwexbgs_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))
df4.to_csv(cwd+"/FINAL/IGNORE/DTWEXBGS_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_ds = pd.read_csv(cwd+"/FINAL/IGNORE/DTWEXBGS_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
df_ds.drop_duplicates(inplace=True)
df_ds = df_ds[df_ds.DTWEXBGS!= "ND"]
df_ds.to_csv(cwd+"/FINAL/DTWEXBGS_FINAL.csv")
df_ds.to_csv(cwd+"/BASE/DTWEXBGS_BASE.csv")

df_ds = pd.read_csv(cwd+"/FINAL/DTWEXBGS_FINAL.csv")
df_ds['DATE'] = pd.to_datetime(df_ds['DATE'])
df_ds= df_ds.set_index('DATE') 
df_ds2=df_ds.drop_duplicates(inplace=False)

df_ds2 = df_ds2[~df_ds2.index.duplicated()]

df_ds2 = df_ds2.resample('D').asfreq()

df_ds2= df_ds2.interpolate(method='linear', axis=0).ffill().bfill()

df_ds2.to_csv(cwd+"/FINAL/DTWEXBGS_FINAL.csv")
df_ds2.to_csv(cwd+"/BASE/DTWEXBGS_BASE.csv")


###############################################################GOLD######################################################################



start_date = date.today()-datetime.timedelta(100)
end_date = date.today()
fx = pdr.get_data_fred("GOLDPMGBD228NLBM", start_date, end_date)

df=pd.DataFrame(fx)
df.columns=['GOLD SPOT']

df.to_csv(cwd+"/FINAL/IGNORE/GOLD_FRED_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/GOLD_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/GOLD_FRED_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


gold_final_hope_2=pd.concat([x3,x4]).drop_duplicates(keep="last").reset_index()
df4=pd.DataFrame(gold_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4.to_csv(cwd+"/FINAL/IGNORE/GOLD_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_gd = pd.read_csv(cwd+"/FINAL/IGNORE/GOLD_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
df_gd.drop_duplicates(inplace=True)
df_gd.to_csv(cwd+"/FINAL/GOLD_FINAL.csv")
df_gd.to_csv(cwd+"/BASE/GOLD_BASE.csv")

df_gd = pd.read_csv(cwd+"/FINAL/GOLD_FINAL.csv")
df_gd['DATE'] = pd.to_datetime(df_gd['DATE'])
df_gd= df_gd.set_index('DATE') 
df_gd2=df_gd.drop_duplicates(inplace=False)

df_gd2 = df_gd2[~df_gd2.index.duplicated()]

df_gd2 = df_gd2.resample('D').asfreq()

df_gd2= df_gd2.interpolate(method='linear', axis=0).ffill().bfill()

df_gd2.to_csv(cwd+"/FINAL/GOLD_FINAL.csv")
df_gd2.to_csv(cwd+"/BASE/GOLD_BASE.csv")




###############################################################VIX############################################################################

start_date = date.today()-datetime.timedelta(100)
end_date = date.today()
fx = pdr.get_data_fred("VIXCLS", start_date, end_date)

df=pd.DataFrame(fx)
df.columns=['VIX']

df.to_csv(cwd+"/FINAL/IGNORE/VIX_FRED_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/VIX_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/VIX_FRED_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


vix_final_hope_2=pd.concat([x3,x4]).drop_duplicates(keep="last").reset_index()
df4=pd.DataFrame(vix_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4.to_csv(cwd+"/FINAL/IGNORE/VIX_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_vx = pd.read_csv(cwd+"/FINAL/IGNORE/VIX_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
df_vx.drop_duplicates(inplace=True)
df_vx.to_csv(cwd+"/FINAL/VIX_FINAL.csv")
df_vx.to_csv(cwd+"/BASE/VIX_BASE.csv")

df_vx = pd.read_csv(cwd+"/FINAL/VIX_FINAL.csv")
df_vx['DATE'] = pd.to_datetime(df_vx['DATE'])
df_vx= df_vx.set_index('DATE') 
df_vx2=df_vx.drop_duplicates(inplace=False)

df_vx2 = df_vx2[~df_vx2.index.duplicated()]

df_vx2 = df_vx2.resample('D').asfreq()

df_vx2= df_vx2.interpolate(method='linear', axis=0).ffill().bfill()

df_vx2.to_csv(cwd+"/FINAL/VIX_FINAL.csv")
df_vx2.to_csv(cwd+"/BASE/VIX_BASE.csv")



##########################################################################USTs#########################################################################

start_date = date.today()-datetime.timedelta(100)
end_date = date.today()
fx = pdr.get_data_fred("DGS10", start_date, end_date)

df=pd.DataFrame(fx)
df.columns=['UST']

df.to_csv(cwd+"/FINAL/IGNORE/UST_FRED_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/UST_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/UST_FRED_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


ust_final_hope_2=pd.concat([x3,x4]).drop_duplicates(keep="last").reset_index()
df4=pd.DataFrame(ust_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4.to_csv(cwd+"/FINAL/IGNORE/UST_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_ut = pd.read_csv(cwd+"/FINAL/IGNORE/UST_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
df_ut.drop_duplicates(inplace=True)
df_ut.to_csv(cwd+"/FINAL/UST_FINAL.csv")
df_ut.to_csv(cwd+"/BASE/UST_BASE.csv")

df_ut = pd.read_csv(cwd+"/FINAL/UST_FINAL.csv")
df_ut['DATE'] = pd.to_datetime(df_ut['DATE'])
df_ut= df_ut.set_index('DATE') 
df_ut2=df_ut.drop_duplicates(inplace=False)

df_ut2 = df_ut2[~df_ut2.index.duplicated()]

df_ut2 = df_ut2.resample('D').asfreq()
df_ut2= df_ut2.interpolate(method='linear', axis=0).ffill().bfill()

df_ut2.to_csv(cwd+"/FINAL/UST_FINAL.csv")
df_ut2.to_csv(cwd+"/BASE/UST_BASE.csv")



##########################################################################SP500#####################################################################

start_date = date.today()-datetime.timedelta(100)
end_date = date.today()
fx = pdr.get_data_fred("SP500", start_date, end_date)

df=pd.DataFrame(fx)
df.columns=['SP500']

df.to_csv(cwd+"/FINAL/IGNORE/SP500_FRED_FINAL.csv",index=True,header=True,index_label="DATE")

x3 = pd.read_csv(cwd+"/BASE/SP500_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/SP500_FRED_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")


sp500_final_hope_2=pd.concat([x3,x4]).drop_duplicates(keep="last").reset_index()
df4=pd.DataFrame(sp500_final_hope_2)
df4 = df4.dropna()
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4.to_csv(cwd+"/FINAL/IGNORE/SP500_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_sp = pd.read_csv(cwd+"/FINAL/IGNORE/SP500_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
df_sp.drop_duplicates(inplace=True)
df_sp.to_csv(cwd+"/FINAL/SP500_FINAL.csv")
df_sp.to_csv(cwd+"/BASE/SP500_BASE.csv")

df_sp = pd.read_csv(cwd+"/FINAL/SP500_FINAL.csv")
df_sp['DATE'] = pd.to_datetime(df_sp['DATE'])
df_sp= df_sp.set_index('DATE') 
df_sp2=df_sp.drop_duplicates(inplace=False)

df_sp2 = df_sp2[~df_sp2.index.duplicated()]

df_sp2 = df_sp2.resample('D').asfreq()
df_sp2= df_sp2.interpolate(method='linear', axis=0).ffill().bfill()

df_sp2.to_csv(cwd+"/FINAL/SP500_FINAL.csv")
df_sp2.to_csv(cwd+"/BASE/SP500_BASE.csv")





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
print(len(df4.DATE))
print(len(set(df4.DATE)))

df4.to_csv(cwd+"/FINAL/IGNORE/CCBTC_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_cc = pd.read_csv(cwd+"/FINAL/IGNORE/CCBTC_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
df_cc.drop_duplicates(inplace=True)
df_cc.to_csv(cwd+"/FINAL/CCBTC_FINAL.csv")
df_cc.to_csv(cwd+"/BASE/CCBTC_BASE.csv")

df_cc = pd.read_csv(cwd+"/FINAL/CCBTC_FINAL.csv")
df_cc['DATE'] = pd.to_datetime(df_cc['DATE'])
df_cc= df_cc.set_index('DATE') 
df_cc2=df_cc.drop_duplicates(inplace=False)

df_cc2 = df_cc2[~df_cc2.index.duplicated()]

df_cc2 = df_cc2.resample('D').asfreq()
df_cc2= df_cc2.interpolate(method='linear', axis=0).ffill().bfill()


df_cc2.to_csv(cwd+"/FINAL/CCBTC_FINAL.csv")
df_cc2.to_csv(cwd+"/BASE/CCBTC_BASE.csv")





################################################################################COMBINED_EXCEL######################################################

new = pd.concat([df_ma2,df_malc2,df_mamc2,df_masc2,df_vg2,df_cp2,df_sp2,df_rt2,df_ds2,df_gd2,df_vx2,df_ut2,df_sp2,df_cc2], axis=1) 
new.to_csv(cwd+"/COMBINED/RAW_DATA.csv")


















