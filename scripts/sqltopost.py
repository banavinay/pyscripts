from queue import *
from threading import Thread
import os	
import csv																																																																																																																																																																																		
import pymysql, sqlparse
import requests
import random 

concurrent = 25
que = Queue(concurrent*25)

# agentlists = ["Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.01",
# 			  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
# 			  "Mozilla/5.0 (Linux; Ubuntu 14.04) AppleWebKit/537.36 Chromium/35.0.1870.2 Safari/537.36",
# 			  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
# 			  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
# 			  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
# 			  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
# 			  "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0"]
# singleagent =  random.choice(agentlists)

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

def DataProcess():
	while True:
		param = que.get()
		
		try:
			# headers = {'User-Agent': 'singleagent',}
			data = {'cin': param['cin']}
			req = requests.post(url="http://13.233.111.58:8000/cvakilapi/v1/company/",data=data)
			print(data, '---->', req.status_code, req.text)	
			if req.status_code == 200 or req.status_code == 201:
				Query("UPDATE CIN_NO set status=1 where CIN='{0}'".format(param['cin']))
		except Exception as e:
			print(e)

		que.task_done()

for i in range(concurrent):
	t = Thread(target=DataProcess)
	t.daemon = True
	t.start()

a = Query("SELECT * FROM CIN_NO where status=0")

for i in a:
	param = {'cin':i['CIN']}
	que.put(param)

que.join()


