#DATABASE AND TABLE CREATION

#import module
import sqlite3

#make connector / create database
mydb=sqlite3.connect("main_db.db")

#execute database query : Create table(relation) with attributes
mydb.execute('''CREATE TABLE IF NOT EXISTS
                            MAIN_PAGE(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            NAME TEXT NOT NULL,
                            USER_NAME TEXT UNIQUE,
                            PASSWORD TEXT NOT NULL
                            )''')

#PRE-DEFINED ACCOUNTS GENERATION
for i in range(10):
    name=input("name: ")
    u_name=input("user_name: ")
    password=input("password: ")
    mydb.execute('''INSERT INTO MAIN_PAGE (NAME, USER_NAME, PASSWORD)
                                VALUES (?, ?, ?)''',(name, u_name, password))


#SAVE CHANGES TO DATABASE
mydb.commit()

#SUCCESSFULLY CLOSE DATABASE
mydb.close()
