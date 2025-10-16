import mysql.connector

mydb = mysql.connector.connect(host="localhost", 
                               user="root", 
                               password="@Yxmr8721")




if mydb.is_connected():
    create = "CREATE DATABASE IF NOT EXISTS alx_book_store"
    mycursor = mydb.cursor()
    mycursor.execute(create)
    print("Database 'alx_book_store' created successfully!")
    mycursor.close()
    mydb.close()
else:
    print("Failed to connect to the database.")
