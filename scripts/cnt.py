import pymysql
import sqlparse
import requests

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


a = Query("SELECT * FROM CIN_NO where status=0")

for i in a:
	try:
		headers = {'Authorization': 'Token df83fd6ba1693b6fbbd035dee56aac89a3f11ecb'}

		data  = {
			'cin': i['CIN']
		}

		req = requests.post(url="http://13.233.111.58:8000/cvakilapi/v1/companyapi/",data=data, headers=headers)
		print(i['status'], '---->', req.status_code)	
		if req.status_code == 200 or req.status_code == 201:
			Query("UPDATE CIN_NO set status=1 where id={0}".format(i['id']))
	except Exception as e:
		print(e)

