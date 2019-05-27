from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import pandas as pd
import os
import shutil
import time
from datetime import datetime, timedelta
import glob
import re
import datetime
from datetime import datetime



#To remove all files from Folder
for root, dirs, files in os.walk('E:/Office Work/04-03-2019/'):
    for f in files:
        os.unlink(os.path.join(root, f))
    for d in dirs:
        shutil.rmtree(os.path.join(root, d))    
#driver = webdriver.Firefox()

#SET Download Path
download_dir = "E:/Office Work/04-03-2019/"
chrome_options = webdriver.ChromeOptions()
preferences = {"download.default_directory": download_dir ,
               "directory_upgrade": True,
               "safebrowsing.enabled": True }
chrome_options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(options=chrome_options)

#Pass FTP URL with Login Credentials
driver.get("ftp://....Your FTP Path")
d = driver.find_element_by_link_text("File_name.xlsx")
#To download FGVGE_Kocher file
d.click()
time.sleep(20)
driver.close()


try:
	#To read file
	for file in glob.glob('E:/Office Work/04-03-2019/Cars24*.xlsx'):
		print("new" + file)
	data_xls = pd.read_excel(file, 'CRM Dump- FGVGE', index_col=None)
	#To specify column to write excel from xlsx
	data_xls2 = data_xls[['Call Date','Source','Appointment ID', 'Mobile']]
	#remove (-) from Appointment_Id column
	data_xls3 = data_xls2.loc[~data_xls2['Appointment ID'].isin(['-'])]
	#1 day before data
	raw_yesterday = datetime.now() - timedelta(days=1)
	yesterday = raw_yesterday.strftime('%Y-%m-%d')
	#filter call_date with max date
	data_xls3 = data_xls3.loc[data_xls3['Call Date'] == yesterday]
	# data_xls3['Call Date'] = pd.to_datetime(data_xls3['Call Date']).dt.strftime('%y-%m-%d')
	# import pdb; pdb.set_trace()
	#Change date format for DB
	data_xls3['Call Date'] = data_xls3['Call Date'].dt.strftime('%Y-%m-%d')
	#write final output to excel
	data_xls3.to_excel('E:/Office Work/04-03-2019/File_name.xlsx', index=False)		
	print('Excel File Saved!')

except Exception as e:
	print(e)