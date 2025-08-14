import requests
from utilities.payload import *
from utilities.resources import *
#config=configparser.ConfigParser()
#config.read('C:\Users\Patil\PycharmProjects\PythonProject\utilities\properties.ini')
#config.read('C:/Users/Patil/PycharmProjects/PythonProject/utilities/properties.ini')''''''
url=getconfig()['API']['apipoint']+'/Library/Addbook.php'
query='select * from Books'
response=requests.post(url,
                       json=buildpayloadfromDB(query),
                       headers={"Content-Type" : "application/json"},)
print("STATUS OF RESPONSE:\n" ,response.status_code) #200
information_of_table=getQuery(query)
print("Information of table been added:\n",information_of_table)
#print(type(response))
try:
    data = response.json()
    print("RESPONSE OF THE API REQUEST:\n",data)  #{'Msg': 'Book Already Exists', 'ID': 'pybgnL228162023'}
except requests.exceptions.JSONDecodeError:
    print("Server did not return JSON. Raw response:")
    print(response.text)
book_id = data['ID']
print("Book ID:", book_id)
 #pybgnL228162023

#get details of all Books
Get_response=requests.get("http://216.10.245.166/Library/GetBook.php",
                          {"AuthorName":"ArthikaPatil"},)

print("LIST OF BOOKS AFTER ADDING BOOK ::\n " ,Get_response.json())
'''[{'book_name': 'Learn Appium Automation with Java', 'isbn': 'AP2816', 'aisle': '2025'},
 {'book_name': 'Python', 'isbn': 'pyt2816', 'aisle': '2025'}, 
 {'book_name': 'SQL for Begineer', 'isbn': 'sql2816', 'aisle': '2025'},
 {'book_name': 'Python for Beginner-L2', 'isbn': 'pybgnl22816', 'aisle': '2023'}
  {'book_name': 'Python for Beginner', 'isbn': 'pybgn2816', 'aisle': '2024'}]
'''
# delete a book
Delete_response=requests.post("http://216.10.245.166/Library/DeleteBook.php",
                              json=payloaddata(book_id),)
Ans=Delete_response.json()
print("Book to be deleted have details as ::\n ", information_of_table )
print("DELETE RESPONSE ::\n ",Ans) #{'msg': 'book is successfully deleted'}
assert Ans['msg'] == 'book is successfully deleted'
#get details of all Books

Get_response=requests.get("http://216.10.245.166/Library/GetBook.php",
                          {"AuthorName":"ArthikaPatil"},)
print("LIST OF BOOKS AFTER DELETING THE SAME BOOK :\n " ,Get_response.json())
'''[{'book_name': 'Learn Appium Automation with Java', 'isbn': 'AP2816', 'aisle': '2025'},
 {'book_name': 'Python', 'isbn': 'pyt2816', 'aisle': '2025'}, 
 {'book_name': 'SQL for Begineer', 'isbn': 'sql2816', 'aisle': '2025'},
 {'book_name': 'Python for Beginner-L2', 'isbn': 'pybgnl22816', 'aisle': '2023'}
  {'book_name': 'Python for Beginner', 'isbn': 'pybgn2816', 'aisle': '2024'}]
'''

