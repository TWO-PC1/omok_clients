import requests, json
import threading
import queue
data = {
    'id': 'jsdjs'
}
headers={}
url='http://127.0.0.1:3000/signin'
url2='http://127.0.0.1:3000/user'
response = requests.get(url, data=json.dumps(data), headers=headers)
print(response.text)
response_data=json.loads(response.text)
headers2 = {'token':response_data.get('token')}

response2 = requests.get(url2, data=json.dumps(data), headers=headers2)
print(response2.text)

