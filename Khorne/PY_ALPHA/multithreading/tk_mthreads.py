##from tkinter import *
##import threading
##import time
##
##
## 
##def tktr(self):
##    app= Tk()
##    app.title("new_app")
##    app.geometry("800x600")
##    app.configure(background="skyblue")
##    lb1=Label(app,font=('Arial',18),text='start')
##    lb1.pack(side=LEFT)
##    app.mainloop()
##
##def nums(self):
##    for i in range(100):
##        lb1.config(text=str(i))
##        print(i)
##        time.sleep(.05)
##        
##
##t1=threading.Thread(target=tktr)
##t2=threading.Thread(target=nums)
##
##t1.start()
##time.sleep(5)
##t2.start()
##t2.join()
##t1.join()

#////
##from tkinter import *
##import threading
##import time
##
##
##class dinesh:
##    def tktr(self):
##        app= Tk()
##        app.title("new_app")
##        app.geometry("800x600")
##        app.configure(background="skyblue")
##        self.lb1=Label(app,font=('Arial',18),text='start')
##        self.lb1.pack(side=LEFT)
##        app.mainloop()
##
##    def nums(self):
##        for i in range(100):
##            self.lb1.config(text=str(i))
##            print(i)
##            time.sleep(.05)
##
##d=dinesh()
##
##t1=threading.Thread(target=d.tktr)
##t2=threading.Thread(target=d.nums)
##
##t1.start()
##time.sleep(5)
##t2.start()
##t2.join()
##t1.join()

#///////////////

##from tkinter import *
##import threading
##import time
##
##
##class dinesh:    
##    def tktr(self):
##        app= Tk()
##        app.title("new_app")
##        app.geometry("800x600")
##        app.configure(background="skyblue")
##        self.lb1=Label(app,font=('Arial',18),text='start')
##        self.lb1.pack(side=LEFT)
##        self.lb2=Label(app,font=('Arial',18),text='start')
##        self.lb2.pack(side=TOP)
##        self.lb3=Label(app,font=('Arial',18),text='start')
##        self.lb3.pack(side=RIGHT)
##        app.mainloop()
##
##    def l2h(self):
##        for i in range(100):
##            self.lb1.config(text=str(i))
##            print('Func 1')
##            time.sleep(.2)
##    def h2l(self):
##        for i in range(100,0,-1):
##            self.lb2.config(text=str(i))
##            print('Func 2')
##            time.sleep(.5)
##    def even(self):
##        for i in range(0,200,2):
##            self.lb3.config(text=str(i))
##            print('Func 3')
##            time.sleep(.05)
##
##d=dinesh()
##
##t1=threading.Thread(target=d.tktr)
##t2=threading.Thread(target=d.l2h)
##t3=threading.Thread(target=d.h2l)
##t4=threading.Thread(target=d.even)
##
##t1.start()
##time.sleep(5)
##t2.start()
##t3.start()
##t4.start()
##t2.join()
##t3.join()
##t4.join()
##t1.join()

#///////////

from tkinter import *
import threading
import time


class dinesh:
    def __init__(self):
        self.stopValue=False
        
    def tktr(self):
        app= Tk()
        app.title("new_app")
        app.geometry("800x600")
        app.configure(background="skyblue")
        self.lb1=Label(app,font=('Arial',18),text='start')
        self.lb1.pack(side=LEFT)
        self.lb2=Label(app,font=('Arial',18),text='start')
        self.lb2.pack(side=TOP)
        self.lb3=Label(app,font=('Arial',18),text='start')
        self.lb3.pack(side=RIGHT)
        app.mainloop()
        self.stopValue=True

    def l2h(self):
        for i in range(100):
            if self.stopValue:
                break
            self.lb1.config(text=str(i))
            print('Func 1')
            time.sleep(.4)
            
    def h2l(self):
        for i in range(100,0,-1):
            if self.stopValue:
                break
            self.lb2.config(text=str(i))
            print('Func 2')
            time.sleep(.5)
            
    def even(self):
        for i in range(0,200,2):
            if self.stopValue:
                break
            self.lb3.config(text=str(i))
            print('Func 3')
            time.sleep(.3)

d=dinesh()

t1=threading.Thread(target=d.tktr)
t2=threading.Thread(target=d.l2h)
t3=threading.Thread(target=d.h2l)
t4=threading.Thread(target=d.even)

t1.start()
time.sleep(5)
t2.start()
t3.start()
t4.start()
t2.join()
t3.join()
t4.join()
t1.join()





