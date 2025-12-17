import mysql.connector

mydb = mysql.connector.connect (
    host= "localhost",
    user= "root",
    password= "055Techsidelegacy3051673"
)

cursor = mydb.cursor()

try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    print("Database 'alx_book_store' created successfully!")
except ConnectionAbortedError:
    print("ERROR: Failed to connect to the database")

cursor.close()
mydb.close()