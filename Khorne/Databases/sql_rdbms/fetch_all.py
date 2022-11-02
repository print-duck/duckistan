import sqlite3
dbase=sqlite3.connect('college.db')
curs=dbase.cursor()


curs.execute('SELECT * FROM TAB1')
data=curs.fetchall()
for i in data:
    print('Id of the student',i[0])
    print('Name of the student',i[1])
    print('Department of the student',i[2])
    print('Register.No of the student',i[3])
    print('\n')


curs.execute('SELECT * FROM TAB1 WHERE DEPT="eie"')
data=curs.fetchall()
print(data)
