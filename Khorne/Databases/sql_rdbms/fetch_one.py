import sqlite3
dbase=sqlite3.connect('college.db')
curs=dbase.cursor()

reg=input('Enter the register number of the student to search: ')
curs.execute('SELECT * FROM TAB1 WHERE REG_NO=?',(reg,))

i=curs.fetchone()

print('Id of the student',i[0])
print('Name of the student',i[1],'\n')
print('Department of the student',i[2])
print("asd \n")
print('Register.No of the student',i[3])
print("\n")
