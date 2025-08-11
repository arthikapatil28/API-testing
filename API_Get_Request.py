import json
import requests

response=requests.get("http://216.10.245.166/Library/GetBook.php",
                      {"AuthorName" : "ArthikaPatil"},)

print(response.text)
print(type(response.text))
result=json.loads(response.text)
print(result)
print(type(result))
print(result[2])
print(result[2]['book_name'])
print(result[2]['isbn'])
'''
#get request using response .json
response=requests.get("http://216.10.245.166/Library/GetBook.php",
             {'AuthorName':"ArthikaPatil"},)'''
resultant=response.json()
print(resultant)
print(type(resultant))
print(resultant[2])
print(resultant[2]['book_name'])
print(resultant[2]['isbn'])
print(response.status_code)
assert response.status_code == 200
print(response.headers)
assert response.headers['Keep-Alive'] == 'timeout=5, max=100'
'''
output : {'Date': 'Mon, 11 Aug 2025 06:59:24 GMT', 'Server': 'Apache', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST',
 'Access-Control-Max-Age': '3600', 'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers,
  Authorization, X-Requested-With', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Transfer-Encoding': 'chunked', 
  'Content-Type': 'application/json;charset=UTF-8'}
To check if the 'Keep-Alive': 'timeout=5, max=100' and vailidate the response add assert'''






