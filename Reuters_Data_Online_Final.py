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

cwd = os.getcwd()
date_month=date.today()
date_today=date.today()-datetime.timedelta(50)



#setting up webdrive

#PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()

########################################################REET#####################################################



dt_string = date_today.strftime("%d/%m/%Y")

my_url="https://sg.finance.yahoo.com/quote/REET/chart/#eyJpbnRlcnZhbCI6ImRheSIsInBlcmlvZGljaXR5IjoxLCJ0aW1lVW5pdCI6bnVsbCwiY2FuZGxlV2lkdGgiOjYuMTE1NjQ2MjU4NTAzNDAyLCJmbGlwcGVkIjpmYWxzZSwidm9sdW1lVW5kZXJsYXkiOnRydWUsImFkaiI6dHJ1ZSwiY3Jvc3NoYWlyIjp0cnVlLCJjaGFydFR5cGUiOiJsaW5lIiwiZXh0ZW5kZWQiOmZhbHNlLCJtYXJrZXRTZXNzaW9ucyI6e30sImFnZ3JlZ2F0aW9uVHlwZSI6Im9obGMiLCJjaGFydFNjYWxlIjoibGluZWFyIiwicGFuZWxzIjp7ImNoYXJ0Ijp7InBlcmNlbnQiOjEsImRpc3BsYXkiOiJSRUVUIiwiY2hhcnROYW1lIjoiY2hhcnQiLCJpbmRleCI6MCwieUF4aXMiOnsibmFtZSI6ImNoYXJ0IiwicG9zaXRpb24iOm51bGx9LCJ5YXhpc0xIUyI6W10sInlheGlzUkhTIjpbImNoYXJ0Iiwi4oCMdm9sIHVuZHLigIwiXX19LCJzZXRTcGFuIjpudWxsLCJsaW5lV2lkdGgiOjIsInN0cmlwZWRCYWNrZ3JvdW5kIjp0cnVlLCJldmVudHMiOnRydWUsImNvbG9yIjoiIzAwODFmMiIsInN0cmlwZWRCYWNrZ3JvdWQiOnRydWUsInJhbmdlIjpudWxsLCJldmVudE1hcCI6eyJjb3Jwb3JhdGUiOnsiZGl2cyI6dHJ1ZSwic3BsaXRzIjp0cnVlfSwic2lnRGV2Ijp7fX0sImN1c3RvbVJhbmdlIjpudWxsLCJzeW1ib2xzIjpbeyJzeW1ib2wiOiJSRUVUIiwic3ltYm9sT2JqZWN0Ijp7InN5bWJvbCI6IlJFRVQiLCJxdW90ZVR5cGUiOiJFVEYiLCJleGNoYW5nZVRpbWVab25lIjoiQW1lcmljYS9OZXdfWW9yayJ9LCJwZXJpb2RpY2l0eSI6MSwiaW50ZXJ2YWwiOiJkYXkiLCJ0aW1lVW5pdCI6bnVsbCwic2V0U3BhbiI6bnVsbH1dLCJzdHVkaWVzIjp7IuKAjHZvbCB1bmRy4oCMIjp7InR5cGUiOiJ2b2wgdW5kciIsImlucHV0cyI6eyJpZCI6IuKAjHZvbCB1bmRy4oCMIiwiZGlzcGxheSI6IuKAjHZvbCB1bmRy4oCMIn0sIm91dHB1dHMiOnsiVXAgVm9sdW1lIjoiIzAwYjA2MSIsIkRvd24gVm9sdW1lIjoiI2ZmMzMzYSJ9LCJwYW5lbCI6ImNoYXJ0IiwicGFyYW1ldGVycyI6eyJ3aWR0aEZhY3RvciI6MC40NSwiY2hhcnROYW1lIjoiY2hhcnQiLCJwYW5lbE5hbWUiOiJjaGFydCJ9fX19"
driver.get(my_url)
driver.maximize_window()

#initializing the action object
action = webdriver.ActionChains(driver)

sleep(2)
driver.execute_script("window.scrollTo(0, 500)") 

#select accept

accept_yahoo=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[contains(concat( " ", @class, " " ), concat( " ", "primary", " " ))]')))
accept_yahoo.click()

#1yr

one_yr=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/section/section/div[1]/div/div[1]/div[2]/ul/li[7]/button')))
one_yr.click()

#grabbing the element and its size and location

element=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/section/section/div[2]/div[12]/div')))

loc=element.location
size=element.size
print(loc)
print(size)

#move the cursor to extreme right of the object

sleep(5)
action.move_to_element(element).perform()
sleep(2)
action.move_by_offset(565,0).perform()

#getting the first date and value pair
date_2=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/section/section/div[2]/div[8]').text

value=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "ciql-price", " " ))]').text

#setting up the dictionary and the limit and pace variables

time_serie=[]
time_serie.append([date_2,value])
#print(time_serie)

limit=dt.datetime.strptime(str(dt_string),'%d/%m/%Y')
pace=-4


#scraping the data
while True:
	action.move_by_offset(pace,0).perform()
	date_2=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/section/section/div[2]/div[8]').text

	value=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "ciql-price", " " ))]').text
	

	

	if dt.datetime.strptime(date_2,'%d/%m/%Y') <limit:

		print(dt.datetime.strptime(date_2,'%d/%m/%Y'))
		break


	if date_2 in time_serie:
		pass
	else:
		time_serie.append([date_2,value])
#driver.quit()
time_serie.reverse()

df3=pd.DataFrame(time_serie,columns=['DATE','REET'])
#df3['DATE'] = pd.to_datetime(df3.DATE)
df3.to_csv(cwd+"/FINAL/IGNORE/REET_YAHOO_FINAL.csv",index=False,header=True,index_label="DATE")



###excel_work####
x3 = pd.read_csv(cwd+"/BASE/REET_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE") 
x4 = pd.read_csv(cwd+"/FINAL/IGNORE/REET_YAHOO_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")



#reet_final_hope_2 = (pd.concat([x3, x4], sort =False).drop_duplicates(['DATE'], keep='last'))



reet_final_hope_2=pd.concat([x3,x4]).drop_duplicates(keep="last").reset_index()
#reet_final_hope_2=x3.append(x4)


df4=pd.DataFrame(reet_final_hope_2)
df4 = df4.dropna()

#print(df8)


#df8.groupby(['DATE'], as_index=False).sum()
#df8.to_excel(cwd+"/BASE/VGTSX_BASE.xlsx",index=False)
df4.to_csv(cwd+"/FINAL/IGNORE/REET_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_rt = pd.read_csv(cwd+"/FINAL/IGNORE/REET_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
print(df_rt)
#df_rt['DATE'] = pd.to_datetime(df_rt['DATE'])
df_rt.drop_duplicates(subset=None, inplace=True)
df_rt.to_csv(cwd+"/FINAL/REET_FINAL.csv")
df_rt.to_csv(cwd+"/BASE/REET_BASE.csv")

df_rt = pd.read_csv(cwd+"/FINAL/REET_FINAL.csv")
df_rt['DATE'] = pd.to_datetime(df_rt['DATE'])
df_rt= df_rt.set_index('DATE') 
df_rt2=df_rt.drop_duplicates(subset=None, inplace=False)
df_rt2 = df_rt2.resample('D').fillna(method = 'bfill')


df_rt2.to_csv(cwd+"/FINAL/REET_FINAL.csv")
df_rt2.to_csv(cwd+"/BASE/REET_BASE.csv")




##############CORP#################################################



dt_string = date_today.strftime("%m%d%Y")

my_url="https://www.cnbc.com/quotes/?symbol=corp-gb"
driver.get(my_url)
driver.maximize_window()


#initializing the action object
action = webdriver.ActionChains(driver)

#grabbing the element and its size and location
sleep(2)
driver.execute_script("window.scrollTo(0, 250)") 


element=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[3]/div[3]/div[1]/div[2]/div/div[2]/div/div[3]/div/div/div[9]/div')))

loc=element.location
size=element.size
print(loc)
print(size)

#move the cursor to extreme right of the object

sleep(5)
action.move_to_element(element).perform()
sleep(2)
action.move_by_offset(355,0).perform()

#getting the first date and value pair
date_2=driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[3]/div[1]/div[2]/div/div[2]/div/div[3]/div/div/div[5]').text

value=driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[3]/div[1]/div[2]/div/div[2]/div/div[3]/div/div/stx-hu-tooltip').text

#setting up the dictionary and the limit and pace variables

time_serie={}
time_serie[date_2]=value.split("\n")
print(time_serie)

limit=dt.datetime.strptime(str(dt_string),'%m%d%Y')
pace=-3

#scraping the data
while True:
	action.move_by_offset(pace,0).perform()
	date_2=driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[3]/div[1]/div[2]/div/div[2]/div/div[3]/div/div/div[5]').text

	value=driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[3]/div[1]/div[2]/div/div[2]/div/div[3]/div/div/stx-hu-tooltip').text




	if dt.datetime.strptime(date_2,'%m-%d-%Y')<limit:
		print(dt.datetime.strptime(date_2,'%m-%d-%Y'))
		break


	if date_2 in time_serie:
		pass
	else:
		time_serie[date_2]=value.split("\n")

#driver.quit()


df1=pd.DataFrame.from_dict(time_serie,orient="index",columns=['Date/Time','CORP','Open','High','Low','Volume'])['CORP'].str.replace("Close","").iloc[::-1]

df1.index.names = ['DATE']
df1.index = pd.to_datetime(df1.index)
df1.to_csv(cwd+'/FINAL/IGNORE/CORP_CNBC_FINAL.csv',index=True,header=True,index_label="DATE")

df1 = pd.read_csv(cwd+'/FINAL/IGNORE/CORP_CNBC_FINAL.csv')
df1=df1.values.tolist()

#df5=pd.DataFrame(df5,columns=['DATE','CORP'])
#df5['DATE'] = pd.to_datetime(df5.DATE)

#df5.to_excel(f'CORP_CNBC_FINAL.xlsx',index=True,header=True,index_label="DATE")



###excel_work####
x1 = pd.read_csv(cwd+"/BASE/CORP_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")

x2 = pd.read_csv(cwd+"/FINAL/IGNORE/CORP_CNBC_FINAL.csv",parse_dates=["DATE"], dayfirst=True,index_col="DATE")


#corp_final_hope_2=x1.append(x2)
corp_final_hope_2=pd.concat([x1,x2]).drop_duplicates(keep="last").reset_index()
df2=pd.DataFrame(corp_final_hope_2)
df2 = df2.dropna()

print(df2)


#df8.groupby(['DATE'], as_index=False).sum()
#df8.to_excel(cwd+"/BASE/VGTSX_BASE.xlsx",index=False)
df2.to_csv(cwd+"/FINAL/IGNORE/CORP_FINAL_IGNORE.csv",index=False)
df_cp = pd.read_csv(cwd+"/FINAL/IGNORE/CORP_FINAL_IGNORE.csv")
df_cp.drop_duplicates(subset=None, inplace=True)
#df_cp['DATE'] = pd.to_datetime(df_cp['DATE'])

df_cp.to_csv(cwd+"/FINAL/CORP_FINAL.csv",index=False)
df_cp.to_csv(cwd+"/BASE/CORP_BASE.csv",index=False)


df_cp = pd.read_csv(cwd+"/FINAL/CORP_FINAL.csv")
df_cp['DATE'] = pd.to_datetime(df_cp['DATE'])
df_cp = df_cp.set_index('DATE') 
df_cp2=df_cp.drop_duplicates(subset=None, inplace=False)
df_cp2 = df_cp2.resample('D').fillna(method = 'bfill')


df_cp2.to_csv(cwd+"/FINAL/CORP_FINAL.csv")
df_cp2.to_csv(cwd+"/BASE/CORP_BASE.csv")





########################SPGSCITR###############################


dt_string = date_today.strftime("%d%m%y")
dt_string_format=dt_string[2]+dt_string[3]+dt_string[0]+dt_string[1]+dt_string[4]+dt_string[5]



my_url="https://www.reuters.com/quote/.SPGSCITR"
driver.get(my_url)
driver.maximize_window()

#initializing the action object
action = webdriver.ActionChains(driver)

def frame_switch(name):
  driver.switch_to.frame(driver.find_element_by_name(name))

agree = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div[2]/div[1]/div[5]/button[2]')))
agree.click()
sleep(2)
driver.switch_to.default_content()


sleep(2)
driver.execute_script("window.scrollTo(0, 450)") 


#grabbing the element and its size and location

element=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[4]/div[1]/div/div/div/div[1]/div[2]/div')))

loc=element.location
size=element.size
print(loc)
print(size)

sleep(5)
action.move_to_element(element).perform()
sleep(2)
action.move_by_offset(216,0).perform()

#getting the first date and value pair
date_2=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "chartworks-legend-timestamp", " " ))]').text

value=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "chartworks-legend-ohlc-c", " " ))]').text

#setting up the dictionary and the limit and pace variables

time_serie=[]
time_serie.append([date_2,value])

#print(date_2,value)

limit=dt.datetime.strptime(str(dt_string_format),'%m%d%y')
pace=-2



#scraping the data
while True:
	action.move_by_offset(pace,0).perform()
	date_2=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "chartworks-legend-timestamp", " " ))]').text

	value=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "chartworks-legend-ohlc-c", " " ))]').text
	




	if dt.datetime.strptime(date_2,'%m/%d/%Y')<limit:
		print(dt.datetime.strptime(date_2,'%m/%d/%Y'))
		break


	if date_2 in time_serie:
		pass
	else:
		time_serie.append([date_2,value])

#driver.quit()

time_serie.reverse()

df5=pd.DataFrame(time_serie,columns=['DATE','SPGSCITR'])
df5["SPGSCITR"].str.replace(',',"")
df5['DATE'] = pd.to_datetime(df5.DATE)
print(df5)

#df5.to_excel(cwd+"/FINAL/IGNORE/SPGSCITR_REUTERS_FINAL.xlsx",index=False,header=True,index_label="DATE")
df5.to_csv(cwd+"/FINAL/IGNORE/SPGSCITR_REUTERS_FINAL.csv",index=False,header=True,index_label="DATE")

###excel_work####
x5 = pd.read_csv(cwd+"/BASE/SPGSCITR_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
#print(x3.sheet_names)
#spgscitr_base_data =x5.parse('Sheet1')

#spgscitr_date=spgscitr_base_data["DATE"]
#spgscitr_value=spgscitr_base_data["SPGSCITR"]


#spgscitr_main_data = []
#for i in range(len(spgscitr_date)):

	#Adding to result based on indexes
#	spgscitr_main_data.append((spgscitr_date[i], spgscitr_value[i]))

#print(reet_main_data)

x6 = pd.read_csv(cwd+"/FINAL/IGNORE/SPGSCITR_REUTERS_FINAL.csv", parse_dates=["DATE"],dayfirst=True,index_col="DATE")
#print(x2.sheet_names)

#spgscitr_new_data =x6.parse('Sheet1')

#spgscitr_new_date=spgscitr_new_data["DATE"]
#spgscitr_new_value=spgscitr_new_data["SPGSCITR"]


#spgscitr_new2_data = []
#for i in range(len(spgscitr_new_date)):

	#Adding to result based on indexes
#	spgscitr_new2_data.append((spgscitr_new_date[i], spgscitr_new_value[i]))

#reet_main_data_s=frozenset(reet_main_data)
#reet_new2_data_s=frozenset(reet_new2_data)

#print(reet_new2_data)

#spgscitr_final_hope_2=x5.append(x6)

spgscitr_final_hope_2=pd.concat([x5,x6]).drop_duplicates(keep="last").reset_index()
#reet_final_hope_2=x3.append(x4)



df6=pd.DataFrame(spgscitr_final_hope_2)
df6 = df6.dropna()

df6.to_csv(cwd+"/FINAL/IGNORE/SPGSCITR_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_sp = pd.read_csv(cwd+"/FINAL/IGNORE/SPGSCITR_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
print(df_sp)
#df_rt['DATE'] = pd.to_datetime(df_rt['DATE'])
df_sp.drop_duplicates(subset=None, inplace=True)
df_sp.to_csv(cwd+"/FINAL/SPGSCITR_FINAL.csv")
df_sp.to_csv(cwd+"/BASE/SPGSCITR_BASE.csv")

df_sp = pd.read_csv(cwd+"/FINAL/SPGSCITR_FINAL.csv")
df_sp['DATE'] = pd.to_datetime(df_sp['DATE'])
df_sp= df_sp.set_index('DATE') 
df_sp2=df_sp.drop_duplicates(subset=None, inplace=False)
df_sp2 = df_sp2.resample('D').fillna(method = 'bfill')


df_sp2.to_csv(cwd+"/FINAL/SPGSCITR_FINAL.csv")
df_sp2.to_csv(cwd+"/BASE/SPGSCITR_BASE.csv")






#################################################################VGTSX###########################################################################################


dt_string = date_today.strftime("%d%m%y")


#opening the connection and grabbing the page
my_url="https://sg.finance.yahoo.com/quote/VT/chart?p=VT&.tsrc=fin-srch#eyJpbnRlcnZhbCI6ImRheSIsInBlcmlvZGljaXR5IjoxLCJ0aW1lVW5pdCI6bnVsbCwiY2FuZGxlV2lkdGgiOjQuNTA1OTI4ODUzNzU0OTQwNSwiZmxpcHBlZCI6ZmFsc2UsInZvbHVtZVVuZGVybGF5Ijp0cnVlLCJhZGoiOnRydWUsImNyb3NzaGFpciI6dHJ1ZSwiY2hhcnRUeXBlIjoibGluZSIsImV4dGVuZGVkIjpmYWxzZSwibWFya2V0U2Vzc2lvbnMiOnt9LCJhZ2dyZWdhdGlvblR5cGUiOiJvaGxjIiwiY2hhcnRTY2FsZSI6ImxpbmVhciIsInBhbmVscyI6eyJjaGFydCI6eyJwZXJjZW50IjoxLCJkaXNwbGF5IjoiVlQiLCJjaGFydE5hbWUiOiJjaGFydCIsImluZGV4IjowLCJ5QXhpcyI6eyJuYW1lIjoiY2hhcnQiLCJwb3NpdGlvbiI6bnVsbH0sInlheGlzTEhTIjpbXSwieWF4aXNSSFMiOlsiY2hhcnQiLCLigIx2b2wgdW5kcuKAjCJdfX0sInNldFNwYW4iOnsibXVsdGlwbGllciI6MSwiYmFzZSI6InllYXIiLCJwZXJpb2RpY2l0eSI6eyJwZXJpb2QiOjEsImludGVydmFsIjoiZGF5In0sIm1haW50YWluUGVyaW9kaWNpdHkiOnRydWUsImZvcmNlTG9hZCI6dHJ1ZX0sImxpbmVXaWR0aCI6Miwic3RyaXBlZEJhY2tncm91bmQiOnRydWUsImV2ZW50cyI6dHJ1ZSwiY29sb3IiOiIjMDA4MWYyIiwic3RyaXBlZEJhY2tncm91ZCI6dHJ1ZSwiZXZlbnRNYXAiOnsiY29ycG9yYXRlIjp7ImRpdnMiOnRydWUsInNwbGl0cyI6dHJ1ZX0sInNpZ0RldiI6e319LCJjdXN0b21SYW5nZSI6bnVsbCwic3ltYm9scyI6W3sic3ltYm9sIjoiVlQiLCJzeW1ib2xPYmplY3QiOnsic3ltYm9sIjoiVlQiLCJxdW90ZVR5cGUiOiJFVEYiLCJleGNoYW5nZVRpbWVab25lIjoiQW1lcmljYS9OZXdfWW9yayJ9LCJwZXJpb2RpY2l0eSI6MSwiaW50ZXJ2YWwiOiJkYXkiLCJ0aW1lVW5pdCI6bnVsbCwic2V0U3BhbiI6eyJtdWx0aXBsaWVyIjoxLCJiYXNlIjoieWVhciIsInBlcmlvZGljaXR5Ijp7InBlcmlvZCI6MSwiaW50ZXJ2YWwiOiJkYXkifSwibWFpbnRhaW5QZXJpb2RpY2l0eSI6dHJ1ZSwiZm9yY2VMb2FkIjp0cnVlfX1dLCJzdHVkaWVzIjp7IuKAjHZvbCB1bmRy4oCMIjp7InR5cGUiOiJ2b2wgdW5kciIsImlucHV0cyI6eyJpZCI6IuKAjHZvbCB1bmRy4oCMIiwiZGlzcGxheSI6IuKAjHZvbCB1bmRy4oCMIn0sIm91dHB1dHMiOnsiVXAgVm9sdW1lIjoiIzAwYjA2MSIsIkRvd24gVm9sdW1lIjoiI2ZmMzMzYSJ9LCJwYW5lbCI6ImNoYXJ0IiwicGFyYW1ldGVycyI6eyJ3aWR0aEZhY3RvciI6MC40NSwiY2hhcnROYW1lIjoiY2hhcnQiLCJwYW5lbE5hbWUiOiJjaGFydCJ9fX19"
driver.get(my_url)
driver.maximize_window()

#initializing the action object
action = webdriver.ActionChains(driver)

sleep(2)
driver.execute_script("window.scrollTo(0, 400)") 

#select 1 yr

#one_yr=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[contains(concat( " ", @class, " " ), concat( " ", "Mstart\(7px\)--tab768", " " )) and (((count(preceding-sibling::*) + 1) = 7) and parent::*)]//spana')))
#one_yr.click()

#1yr

one_yr=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/section/section/div[1]/div/div[1]/div[2]/ul/li[7]/button')))
one_yr.click()

#grabbing the element and its size and location

element=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/section/section/div[2]/div[12]/div')))

loc=element.location
size=element.size
print(loc)
print(size)

#move the cursor to extreme right of the object

sleep(5)
action.move_to_element(element).perform()
sleep(2)
action.move_by_offset(565,0).perform()

#getting the first date and value pair
date_2=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/section/section/div[2]/div[8]').text

value=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "ciql-price", " " ))]').text

#setting up the dictionary and the limit and pace variables

time_serie=[]
time_serie.append([date_2,value])
#print(time_serie)

limit=dt.datetime.strptime(str(dt_string),'%d%m%y')
pace=-4

#scraping the data
while True:
	action.move_by_offset(pace,0).perform()
	date_2=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/section/section/div[2]/div[8]').text

	value=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "ciql-price", " " ))]').text
	

	

	if dt.datetime.strptime(date_2,'%d/%m/%Y') <limit:
		print(dt.datetime.strptime(date_2,'%d/%m/%Y'))
		break


	if date_2 in time_serie:
		pass
	else:
		time_serie.append([date_2,value])

driver.quit()
time_serie.reverse()

df7=pd.DataFrame(time_serie,columns=['DATE','VGTSX'])
#df7['DATE'] = pd.to_datetime(df7.DATE)

#df7.to_excel(cwd+"/FINAL/IGNORE/VGTSX_YAHOO_FINAL.xlsx",index=False,header=True,index_label="DATE")
df7.to_csv(cwd+"/FINAL/IGNORE/VGTSX_YAHOO_FINAL.csv",index=False,header=True,index_label="DATE")

###excel_work####



x7 = pd.read_csv(cwd+"/BASE/VGTSX_BASE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
#print(x7)
#print(x7.sheet_names)

#vgtsx_base_data =x7.parse('Sheet1')

#vgtsx_date=vgtsx_base_data["DATE"]
#print(vgtsx_date)

#vgtsx_value=vgtsx_base_data["VGTSX"]


#vgtsx_main_data = []
#for i in range(len(vgtsx_date)):

#	#Adding to result based on indexes
#	vgtsx_main_data.append((vgtsx_date[i], vgtsx_value[i]))

#print(reet_main_data)


x8 = pd.read_csv(cwd+"/FINAL/IGNORE/VGTSX_YAHOO_FINAL.csv", parse_dates=["DATE"], dayfirst=True,index_col="DATE")
#x8 = pd.ExcelFile(cwd+"/FINAL/IGNORE/VGTSX_YAHOO_FINAL.xlsx")
#print(x2.sheet_names)

#vgtsx_new_data =x8.parse('Sheet1')

#vgtsx_new_date=vgtsx_new_data["DATE"]
#print(vgtsx_new_date)

#vgtsx_new_value=vgtsx_new_data["VGTSX"]


#vgtsx_new2_data = []
#for i in range(len(vgtsx_new_date)):

#	#Adding to result based on indexes
#	vgtsx_new2_data.append((vgtsx_new_date[i], vgtsx_new_value[i]))


vgtsx_final_hope_2=pd.concat([x7,x8]).drop_duplicates(keep="last").reset_index()
df8=pd.DataFrame(vgtsx_final_hope_2)
df8 = df8.dropna()


df8.to_csv(cwd+"/FINAL/IGNORE/VGTSX_FINAL_IGNORE.csv",index=False,header=True,index_label="DATE")
df_vg = pd.read_csv(cwd+"/FINAL/IGNORE/VGTSX_FINAL_IGNORE.csv",parse_dates=["DATE"],dayfirst=True,index_col="DATE")
print(df_vg)
#df_rt['DATE'] = pd.to_datetime(df_rt['DATE'])
df_vg.drop_duplicates(subset=None, inplace=True)
df_vg.to_csv(cwd+"/FINAL/VGTSX_FINAL.csv")
df_vg.to_csv(cwd+"/BASE/VGTSX_BASE.csv")

df_vg = pd.read_csv(cwd+"/FINAL/VGTSX_FINAL.csv")
df_vg['DATE'] = pd.to_datetime(df_vg['DATE'])
df_vg= df_vg.set_index('DATE') 
df_vg2=df_vg.drop_duplicates(subset=None, inplace=False)
df_vg2 = df_vg2.resample('D').fillna(method = 'bfill')


df_vg2.to_csv(cwd+"/FINAL/VGTSX_FINAL.csv")
df_vg2.to_csv(cwd+"/BASE/VGTSX_BASE.csv")


##############################################combined_excel_sheet###########################################################################


new = pd.concat([df_rt2,df_cp2,df_sp2,df_vg2], axis=1) 
new.to_csv(cwd+"/COMBINED/REUTERS_COMBINED.csv")




















