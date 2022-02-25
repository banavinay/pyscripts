import threading
from threading import *
import time
import os, shutil
import pymysql, sqlparse

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

def thread1():
	directory_path = '/var/www/seleniumtest/data1'
	destination = '/var/www/seleniumtest/dataccc'

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
						print(ww,'thread1')
						try:
							Query('INSERT INTO CIN_NO(CIN) VALUES("'+str(ww)+'")')
						except Exception as e:
							print(e)
				
				i +=1
			shutil.move(name1, name2)


def thread2():

	directory_path = '/var/www/seleniumtest/data2'
	destination = '/var/www/seleniumtest/dataccc'

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
						print(ww,'thread2')
						try:
							Query('INSERT INTO CIN_NO(CIN) VALUES("'+str(ww)+'")')
						except Exception as e:
							print(e)
				
				i +=1
			shutil.move(name1, name2)

def thread3():
	directory_path = '/var/www/seleniumtest/data'
	destination = '/var/www/seleniumtest/dataccc'

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
						print(ww,'thread3')
						try:
							Query('INSERT INTO CIN_NO(CIN) VALUES("'+str(ww)+'")')
						except Exception as e:
							print(e)
				
				i +=1
			shutil.move(name1, name2)

def thread4():
	directory_path = '/var/www/seleniumtest/data3'
	destination = '/var/www/seleniumtest/dataccc'

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
						print(ww,'thread4')
						try:
							Query('INSERT INTO CIN_NO(CIN) VALUES("'+str(ww)+'")')
						except Exception as e:
							print(e)
				
				i +=1
			shutil.move(name1, name2)

t1=Thread(target=thread1)
t2=Thread(target=thread2)
t3=Thread(target=thread3)
t4=Thread(target=thread4)
t1.start()
time.sleep(1)
t2.start()
time.sleep(1)
t3.start()
time.sleep(1)
t4.start()