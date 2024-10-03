import mysql.connector
from mysql.connector import Error
import datetime

def connect():
    connection = None
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user='root',
            password='123456789',
            database='movie'
        )
        print('Connection successful!')
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection





