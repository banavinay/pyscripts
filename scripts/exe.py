from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time 
import csv
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


prefs = {"download.default_directory" : '/var/www/seleniumtest/archive/'}

options = Options()			
options.add_argument("--start-maximized")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option("prefs",prefs)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--silent")

browser = webdriver.Chrome('/var/www/chromedriver', options=options)



browser.get('https://www.mca.gov.in/MinistryV2/eir_archive.html')
# browser.find_element_by_class_name("rules").click()
time.sleep(5)
total_file = browser.find_element_by_id("example_info").text
total_count = total_file.split(' ')[5]
total_page = (int(total_count)//6)+1
for i in range(total_page):

	excelfiles = browser.find_elements_by_class_name("descinner")
	action = ActionChains(browser);
	for excelfile in excelfiles:
		excelfile.click()
		time.sleep(2)

		print(excelfile.text)
	i+=1;
	pagination = browser.find_element_by_id("example_next")
	browser.execute_script("arguments[0].click();", pagination)
	time.sleep(10)