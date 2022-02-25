# from selenium import webdriver 
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# import time 
import csv
import os, shutil
from urllib.parse import urljoin, urlparse
import urllib.request
import pymysql, sqlparse
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException


# prefs = {"download.default_directory" : '/var/www/seleniumtest/excel/'}

# options = Options()			
# options.add_argument("--start-maximized")
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')
# options.add_experimental_option("prefs",prefs)
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--silent")

def Query(sql):
	db = pymysql.connect("localhost","root","stroops2020","CIN_Number",charset='utf8mb4')
	dbc = db.cursor(pymysql.cursors.DictCursor)
	output = {}
	qcnt = -1
	for statement in sqlparse.split(sql):
		qcnt = qcnt + 1
		dbc.execute(statement)
		db.commit()
		output[qcnt] = dbc.fetchall()
	if qcnt == 0:
		output = output[0]
	dbc.close()
	db.close()
	return output

# browser = webdriver.Chrome('/var/www/chromedriver', options=options)

directory_path = '/var/www/seleniumtest/data'
destination = '/var/www/seleniumtest/datacom'

for filename in os.listdir(directory_path):
	print(filename)
	name1=  directory_path+'/'+ filename
	name2 = destination +'/'+ filename

	# file_upload(os.path.join(directory_path, filename))
	with open(name1, encoding="utf8", errors='ignore') as f:
		data = f.read()
		i = 0
		for row in data.split('\n'):
			if row != '':
				if i > 0:
					cin= row.split(',')[0]
					ww = cin.replace("'",'').replace('"','')
					print(ww)
					try:
						Query('INSERT INTO CIN_NO(CIN) VALUES("'+str(ww)+'")')
					except Exception as e:
						print(e)
			
			i +=1
		shutil.move(name1, name2) 



# browser.get('https://www.mca.gov.in/MinistryV2/incorporatedorclosedduringthemonth.html')
# browser.find_element_by_class_name("rules").click()
# time.sleep(5)
# total_file = browser.find_element_by_id("example_info").text
# print(total_file)
# total_count = total_file.split(' ')[5]
# print(total_count)
# total_page = (int(total_count)//6)+1
# print(total_page)
# for i in range(total_page):

# 	excelfiles = browser.find_elements_by_class_name("descinner")
# 	action = ActionChains(browser);
# 	print(excelfiles)
# 	for excelfile in excelfiles:
# 		print('heeeeeeeeeeeee')
# 		excelfile.click()
# 		time.sleep(2)

# 		print(excelfile.text)
# 	i+=1;
# 	pagination = browser.find_element_by_id("example_next")
# 	browser.execute_script("arguments[0].click();", pagination)
# 	time.sleep(10)

	
