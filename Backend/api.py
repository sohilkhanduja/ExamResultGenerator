import requests
import json

try:
	wa = " http://192.168.1.102:5000/check"
	id = int(input('Enter roll no: '))
	password = input('Enter password: ')
    
	data = {'id':id, "password":password}
	res = requests.post(wa,json=json.dumps(data))
	print(res)

	data = res.json()
	ans =data['msg']
	print(ans)

except Exception as e:
	print(e)