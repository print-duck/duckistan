#creating table and inserting values
import sqlite3
dbase=sqlite3.connect('college.db')
dbase.execute('''CREATE TABLE IF NOT EXISTS
                            TAB1(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            NAME TEXT NOT NULL,
                            DEPT TEXT NOT NULL,
                            REG_NO TEXT UNIQUE
                            )''')
dbase.execute('''CREATE TABLE IF NOT EXISTS
                            TAB2(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            NAME TEXT NOT NULL,
                            DEPT TEXT NOT NULL,
                            REG_NO TEXT UNIQUE
                            )''')
n=int(input('How many students to add: '))
for i in range(n):
    name=input('Enter the Name: ')
    dept=input('Enter the Department: ')
    register=input('Enter the Register Number: ')
    dbase.execute('INSERT INTO TAB1 (NAME,DEPT,REG_NO) VALUES (?,?,?)',(name,dept,register))
dbase.commit()
#dbase.close()
