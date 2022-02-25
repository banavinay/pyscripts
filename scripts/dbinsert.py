from queue import *
from threading import Thread
import os	
import csv																																																																																																																																																																																		
import pymysql, sqlparse

concurrent = 50
que = Queue(concurrent*50)

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
		cin = param['cin']
		print("processing....", cin)
		try:
			Query('INSERT INTO CIN_NO(CIN) VALUES("'+str(cin)+'")')
		except Exception as e:
			print(e)

		que.task_done()

for i in range(concurrent):
	t = Thread(target=DataProcess)
	t.daemon = True
	t.start()

with open("/var/www/seleniumtest/data4/indian_company.csv", encoding="utf8", errors='ignore') as f:
	data = csv.reader(f)
	for row in data:
		param = {'cin':row[1]}
		que.put(param)

que.join()


