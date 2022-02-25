from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time 
import csv
from selenium.webdriver.chrome.options import Options


prefs = {"download.default_directory" : '/var/www/seleniumtest/data/'}

options = Options()			
options.add_argument("--start-maximized")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option("prefs",prefs)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--silent")

browser = webdriver.Chrome('/var/www/chromedriver', options=options)



browser.get('https://data.gov.in/catalog/company-master-data?filters%5Bfield_catalog_reference%5D=354261&format=json&offset=0&limit=6&sort%5Bcreated%5D=desc')

total_file = browser.find_element_by_class_name("view-header").text
total_count = total_file.split(' ')[4]
total_page = (int(total_count)//6)+1
print(total_page)
for i in range(total_page):

	csvfiles = browser.find_elements_by_link_text("csv")
	action = ActionChains(browser);
	print(csvfiles)
	for csvfile in csvfiles:
		browser.execute_script("arguments[0].click();", csvfile)
		time.sleep(5)

		selector1 = browser.find_element_by_id("edit-download-reasons-1")
		browser.execute_script("arguments[0].click();", selector1)
		time.sleep(1)

		selector2 = browser.find_element_by_id("edit-reasons-d-4")
		browser.execute_script("arguments[0].click();", selector2)

		nameinput= browser.find_element_by_id("edit-name-d")
		nameinput.send_keys('luhegytti')

		mailinput = browser.find_element_by_id("edit-mail-d")
		mailinput.send_keys('luhegytti-0826@yopmail.com')

		submitinput = browser.find_element_by_id("edit-submit")
		submitinput.click()

		time.sleep(5)
		browser.switch_to.window(browser.window_handles[1])
		browser.close()
		time.sleep(5)
		browser.switch_to.window(browser.window_handles[0])

		print(csvfile.text)
	i+=1;
	pagination = browser.find_element_by_link_text("Next")
	browser.execute_script("arguments[0].click();", pagination)
	time.sleep(10)


# with open("/var/www/seleniumtest/data/Data_Gov_Chattisgarh.CSV",  encoding="utf8", errors='ignore') as f:
# 	data = f.read()
# 	i = 0
# 	for row in data.split('\n'):
# 		if row != '':
# 			if i > 0:
# 				cin= row.split(',')[0]
# 				print(cin.replace("'",'').replace('"',''))

# 			i +=1