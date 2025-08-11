import requests
from payload import *
response=requests.post("http://216.10.245.166/Library/Addbook.php",
                       json={"name":"Python for Beginner-L4",
                             "isbn":"pybgnL42816",
                             "aisle":"2021",
                             "author":"ArthikaPatil"},
                       headers={"Content-Type" : "application/json"},)
print("STATUS OF RESPONSE" ,response.status_code) #200
#print(type(response))
try:
    data = response.json()
    print("RESPONSE OF THE API REQUEST",data)  #{'Msg': 'Book Already Exists', 'ID': 'pybgnL228162023'}
except requests.exceptions.JSONDecodeError:
    print("Server did not return JSON. Raw response:")
    print(response.text)
book_id = data['ID']
print("Book ID:", book_id)
 #pybgnL228162023

#get details of all Books
Get_response=requests.get("http://216.10.245.166/Library/GetBook.php",
                          {"AuthorName":"ArthikaPatil"},)

print("LIST OF BOOKS AFTER ADDING BOOK : " ,Get_response.json())
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
print("DELETE RESPONSE : ",Ans) #{'msg': 'book is successfully deleted'}
assert Ans['msg'] == 'book is successfully deleted'
#get details of all Books

Get_response=requests.get("http://216.10.245.166/Library/GetBook.php",
                          {"AuthorName":"ArthikaPatil"},)
print("LIST OF BOOKS AFTER DELETING THE SAME BOOK : " ,Get_response.json())
'''[{'book_name': 'Learn Appium Automation with Java', 'isbn': 'AP2816', 'aisle': '2025'},
 {'book_name': 'Python', 'isbn': 'pyt2816', 'aisle': '2025'}, 
 {'book_name': 'SQL for Begineer', 'isbn': 'sql2816', 'aisle': '2025'},
 {'book_name': 'Python for Beginner-L2', 'isbn': 'pybgnl22816', 'aisle': '2023'}
  {'book_name': 'Python for Beginner', 'isbn': 'pybgn2816', 'aisle': '2024'}]
'''

