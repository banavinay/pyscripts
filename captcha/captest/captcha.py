from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.chrome.options import Options
from PIL import Image 
import cv2
import pytesseract
import io

def getDetail(browser,img_name):	
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  #scrolls page down	
	cap_img = browser.find_element_by_id('Captcha').screenshot_as_png  #find the captcha element & saves screenshot in bytes	
	imageStream = io.BytesIO(cap_img)  #convert bytes into image	
	im = Image.open(imageStream)  #opens the image 	
	im.save(img_name,'png')  #saves as img_name	
	img = cv2.imread(img_name, 0)   #rectify captcha image, remove dots and lines in background of captcha image
	ret,thresh = cv2.threshold(img,55,255,cv2.THRESH_BINARY)
	opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT,(2,2)))	
	cv2.imwrite('captcha.png', opening)  #saves the rectified image as captcha.png	
	pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  #used to read text of image	
	cap_text = pytesseract.image_to_string(Image.open(img_name),lang='eng')  #converts text of image into string
	browser.find_element_by_id('CaptchaText').send_keys(cap_text)   #find input for captcha text and enter captcha text
	try:
		browser.find_element_by_name('submit').click()    #clicks on submit button
	except:
		return cap_text
	time.sleep(2)
	try:
		time.sleep(2)
		browser.find_element_by_id('tableData')   #try to find element at new page after sucessfully submiting the captcha
	except Exception as e:
		getDetail(browser,img_name)     #if captcha is not correct,recall the function

options = Options()			
options.add_argument("--start-maximized")

browser = webdriver.Chrome('./chromedriver', options=options)    #opens the browser
browser.get('https://ipindiaservices.gov.in/PublicSearch')     #opens the mentioned url
startingdate = browser.find_element_by_id("FromDate")    #finds a date input
startingdate.send_keys('01/01/1800')      #send date to input field
enddate = browser.find_element_by_id("ToDate")     #finds a date input
enddate.send_keys('12/29/2020')   #send date to input field
getDetail(browser,'captcha.png')   #it will call the function of captcha
time.sleep(10)
print("captcha has been by passed successfully")
browser.quit()  #quits the browser