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

date_today=date.today()-datetime.timedelta(2)

dt_string = date_today.strftime("%m/%d")




#setting up webdrive

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


#opening the connection and grabbing the page
my_url="https://www.google.com/webhp?hl=en"
driver.get(my_url)
driver.maximize_window()

#initializing the action object
action = webdriver.ActionChains(driver)

#performing the search

search_bar=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')))

#search_button=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/form/div[2]/div[1]/div[3]/center/input[1]')))

search_bar.send_keys('reet')
search_bar.send_keys(Keys.RETURN)


sleep(2)

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

date_today=date.today()-datetime.timedelta(30)

dt_string = date_today.strftime("%m/%d")




#setting up webdrive

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


#opening the connection and grabbing the page
my_url="https://www.google.com/webhp?hl=en"
driver.get(my_url)
driver.maximize_window()

#initializing the action object
action = webdriver.ActionChains(driver)

#performing the search

search_bar=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')))

#search_button=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/form/div[2]/div[1]/div[3]/center/input[1]')))

search_bar.send_keys('reet')
search_bar.send_keys(Keys.RETURN)


sleep(2)

#selecting 1m

month=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/g-card-section[1]/div/div[1]/div/div[4]/div')))

month.click()

#grabbing the element and its size and location

#grabbing the element and its size and location

element=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/g-card-section[1]/div/div[2]')))

loc=element.location
size=element.size
print(loc)
print(size)

#move the cursor to extreme right of the object

sleep(5)
action.move_to_element_with_offset(element,640,0).perform()

#getting the first date and value pair
date_2=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "knowledge-finance-wholepage-chart__hover-card-time", " " ))]').text

value=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "knowledge-finance-wholepage-chart__hover-card-value", " " ))]').text

#setting up the dictionary and the limit and pace variables

time_serie={}
time_serie[date_2]=value

print(date_2,value)









limit=dt.datetime.strptime(str(dt_string),'%m/%d')
pace=-5



#scraping the data
while True:
	action.move_by_offset(pace,0).perform()
	date_2=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "knowledge-finance-wholepage-chart__hover-card-time", " " ))]').text

	value=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "knowledge-finance-wholepage-chart__hover-card-value", " " ))]').text

	

	if dt.datetime.strptime(date_2,'%a, %d %b') <limit:
		print(dt.datetime.strptime(date_2,'%a, %d %b'))
		break


	if date_2 in time_serie:
		pass
	else:
		time_serie[date_2]=value

driver.quit()

df=pd.DataFrame.from_dict(time_serie,orient='index',columns=['values'])
df.to_csv('reet_google.csv')













