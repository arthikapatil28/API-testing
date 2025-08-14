import mysql.connector
import configparser
from mysql.connector import Error

#used to get the id of book to be deleted in API_POST_Request
def payloaddata(book_id):
    body = {
        'ID': book_id
    }
    return body
#used to get the full row details of book in dictionary as json input  in API_POST_Request
def addBookpayload():
    Fbody={"name":"Python for Beginner-L4",
            "isbn":"pybgnL42816",
            "aisle":"2021",
            "author":"ArthikaPatil"
    }
    return Fbody
# used to read the hosts from propeties.ini file
def getconfig():
    config=configparser.ConfigParser()
    config.read('C:/Users/Patil/PycharmProjects/PythonProject/utilities/properties.ini')
    return config
#dictionory to give as input for the getconnection fucn
connect_config={'host':getconfig()['SQL']['host'],
                'database':getconfig()['SQL']['database'],
                'user':getconfig()['SQL']['user'],
                'password':getconfig()['SQL']['password'],}
# used in BD query file for connection
def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)  #** re[represents it is a dictionary
        if conn.is_connected():
            print("Connection Successful")
            return conn
    except Error as e:
        print(e)
#while fetching table from database to give a json dict need connection
def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row=cursor.fetchone()
    conn.close()
    return row

# connection and retrive data from db
def buildpayloadfromDB(query):
    addBody={}
    tp=getQuery(query)
    addBody['name']=tp[0]
    addBody['isbn']=tp[1]
    addBody['aisle']=tp[2]
    addBody['author']=tp[3]
    return addBody



