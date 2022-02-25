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

directory_path = '/var/www/seleniumtest/data4'
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
					cin= row.split(',')[1]
					print(cin)
					ww = cin.replace("'",'').replace('"','')
					print(ww)
					# try:
					# 	Query('INSERT INTO CIN_NO(CIN) VALUES("'+str(ww)+'")')
					# except Exception as e:
					# 	print(e)
			
			i +=1
		# shutil.move(name1, name2)
