from tkinter import *
from PIL import Image,ImageTk
import sqlite3
dbase=sqlite3.connect("student deatils.db")
dbase.execute("""CREATE TABLE IF NOT EXISTS
                 TABLE1(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NAME TEXT NOT NULL,
                        DEPT TEXT NOT NULL,
                        REGNO TEXT UNIQUE)""")
dbase.commit()
app=Tk()
app.title("my app")
app.geometry("1366x768")
app.configure(background="skyblue")
bg_image=Image.open("my image1.png")
test_img=ImageTk.PhotoImage(bg_image)
name=StringVar()
dept=StringVar()
regno=StringVar()
sregno=StringVar()
def submit():
	nameval=name.get()
	print(nameval)
	deptval=dept.get()
	print(deptval)
	regnoval=regno.get()
	print(regnoval)
	dbase.execute("INSERT  INTO TABLE1(NAME,DEPT,REGNO)VALUES(?,?,?)",(nameval,deptval,regnoval))
	dbase.commit()
	ent1.delete(first=0,last=END)
	ent2.delete(first=0,last=END)
	ent3.delete(first=0,last=END)
	

def search():
      sregnoval=sregno.get()
      ent4.delete(first=0,last=END)
      print(sregnoval)
      con=dbase.cursor()
      con.execute("SELECT*FROM TABLE1 WHERE REGNO=?",(sregnoval,))
      value=con.fetchone()
      #print(value)
      if value:
            print("ID:",value[0])
            print("name:",value[1])
            print("dept:",value[2])
            print("regno:",value[3])
      
            subapp=Toplevel(app)
            subapp.title("my subapp")
            subapp.geometry("600x300")
            subapp.configure(background="skyblue")
            lb1=Label(subapp,text="name:",font=("Georgia",26),bg="skyblue",fg="#663300")
            lb1.place(x=50,y=100)

            lb2=Label(subapp,text="dept:",font=("Georgia",26),bg="skyblue",fg="#663300")
            lb2.place(x=50,y=150)

            lb3=Label(subapp,text="rego:",font=("Georgia",26),bg="skyblue",fg="#663300")
            lb3.place(x=50,y=200)

            lb4=Label(subapp,text=value[1],font=("Georgia",26),bg="skyblue",fg="#663300")
            lb4.place(x=160,y=100)

            lb5=Label(subapp,text=value[2],font=("Georgia",26),bg="skyblue",fg="#663300")
            lb5.place(x=150,y=150)

            lb6=Label(subapp,text=value[3],font=("Georgia",26),bg="skyblue",fg="#663300")
            lb6.place(x=150,y=200)
            
      
            subapp.mainloop()
      else:
            print("entered register number ia not found")

      
      


bg_lb=Label(app,image=test_img)
bg_lb.place(x=0,y=0,relwidth=1,relheight=1)
lb1=Label(app,text="enter the name",font=("Georgia",26),bg="skyblue",fg="#663300")
lb1.place(x=50,y=100)
ent1=Entry(app,textvariable=name,font=("Georgia",26))
ent1.place(x=450,y=100)


lb2=Label(app,text="enter the dept",font=("Georgia",26),bg="skyblue",fg="#663300")
lb2.place(x=50,y=200)
ent2=Entry(app,textvariable=dept,font=("Georgia",26))
ent2.place(x=450,y=200)



lb3=Label(app,text="enter the regno",font=("Georgia",26),bg="skyblue",fg="#663300")
lb3.place(x=50,y=300)
ent3=Entry(app,textvariable=regno,font=("Georgia",26))

ent3.place(x=450,y=300)

btn1=Button(app,command=submit,text="submit",font=("Georgia",16),bg="green",fg="white",activebackground="red",activeforeground="yellow",width=10,bd=5)
btn1.place(x=600,y=400)

lb4=Label(app,text="enter the  search regno",font=("Georgia",26),bg="skyblue",fg="#663300")
lb4.place(x=50,y=500)
ent4=Entry(app,textvariable=sregno,font=("Georgia",26))
ent4.place(x=450,y=500)

btn2=Button(app,command=search,text="search",font=("Georgia",16),bg="green",fg="white",activebackground="red",activeforeground="yellow",width=10,bd=5)
btn2.place(x=600,y=600)



app.mainloop()
dbase.close()
