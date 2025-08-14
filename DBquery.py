import _mysql_connector
import mysql.connector

from utilities.payload import *

#host,database,user,password
#conn=mysql.connector.connect(host='localhost',database='APIDevelop',user='root',password='password')
conn=getConnection()
print(conn.is_connected())
cursor=conn.cursor()
#cursor.execute('select * from CustomerInfo')
print(cursor.fetchone())
rows=cursor.fetchall()
print("Total details of table: \n", rows)
sum=0
for row in rows:
    #print(row)
    name=row[0]
    amt=row[2]
    print(f"Amount of {name} is : {amt}")
    sum=sum+row[2]
print("Total Amount of All books together :",sum)
#Update the table with new location 
query="UPDATE CustomerInfo SET Location = %s WHERE CourseName = %s"
data=("US","WebServices")
cursor=cursor.execute(query,data)
conn.commit() #commit should be done at connection level

#Delete the table with new location
query="Delete from CustomerInfo WHERE CourseName = %s"
data=("WebServices",)
cursor=cursor.execute(query,data)
conn.commit()

cursor.execute('select * from CustomerInfo')
rows=cursor.fetchall()
print("Total details of table: \n", rows)
conn.close()