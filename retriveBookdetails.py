import json
import requests

response=requests.get("http://216.10.245.166/Library/GetBook.php",
                      {"AuthorName" : "ArthikaPatil"},)
resultant=response.json()
# Retrive the book with isbn 'pyt2816' and return complete book details
for Abook in resultant:
    if Abook['isbn']=='pyt2816':
        print(Abook)
        break
        #print("Abook in if " ,Abook)
eBook={
        "book_name": "Python",
        "isbn": "pyt2816",
        "aisle": "2025"
    }
assert eBook==Abook


