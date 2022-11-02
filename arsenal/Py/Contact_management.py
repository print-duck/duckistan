from tkinter import*
from tkinter import messagebox
import sqlite3
dbase=sqlite3.connect('prawin.db')
dbase.execute('''CREATE TABLE IF NOT EXISTS
               TAB1(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               NAME TEXT NOT NULL,
               DEPT TEXT NOT NULL,
               REGNO TEXT UNIQUE)''')
dbase.commit()

app=Tk()
app.title('IPL')
app.geometry('800x400')
app.configure(background='#6ac2e9')

name=StringVar()
dept=StringVar()
regno=IntVar()

def submit():
      nameval=name.get()
      deptval=dept.get()
      regnoval=regno.get()
      
      print(nameval)
      print(deptval)
      print(regnoval)
      dbase.execute('INSERT INTO TAB1(NAME,DEPT,REGNO)VALUES(?,?,?)',(nameval,deptval,regnoval))
      dbase.commit()
      
      messagebox.showinfo('sucess','your have insert successfully')



lb1=Label(app,text='Enter your name : ',font=('Arial',28),bg='#6ac2e9',fg='red')
lb1.grid(row=0,column=0,padx=15,pady=15)
ent1=Entry(app,font=('Arial',28),bg='green',fg='pink',textvariable=name)
ent1.grid(row=0,column=2,padx=15,pady=15)
lb2=Label(app,text='Enter your dept : ',font=('Jokerman',28),bg='#6ac2e9',fg='red')
lb2.grid(row=1,column=0,padx=15,pady=15)
ent2=Entry(app,font=('Arial',28),bg='green',fg='pink',textvariable=dept)
ent2.grid(row=1,column=2,padx=15,pady=15)
lb3=Label(app,text='Enter your regno : ',font=('Jokerman',28),bg='#6ac2e9',fg='red')
lb3.grid(row=2,column=0,padx=15,pady=15)
ent3=Entry(app,font=('Arial',28),bg='green',fg='pink',textvariable=regno)
ent3.grid(row=2,column=2,padx=15,pady=15)


btn=Button(app,text='submit',font=('Arial',28),bg='#6ac2e9',fg='red',command=submit,activebackground='yellow')
btn.grid(row=3,column=2)




app.mainloop()
