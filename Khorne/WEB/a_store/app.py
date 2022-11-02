#import neccessary modules
from flask import Flask, render_template,request
from sqlite3 import *
#Initiate Flask Object
app=Flask(__name__)
#Initiate Sqlite Object
base=connect('base.db', check_same_thread=False)
base.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             mail TEXT NOT NULL UNIQUE,
             phone INTEGER UNIQUE,
             username TEXT NOT NULL UNIQUE,
             password TEXT NOT NULL);''')
#Create Cursor to get data from specific records
cr=base.cursor()



#Create the first html page direction
@app.route('/',methods=['GET','POST'])
def home():
    #to get login details from main.html and redirection depending upon data
    return render_template('main.html')


@app.route('/t',methods=['GET','POST'])
def ticket():
    if request.method=='POST':
        lname=request.form['uname']
        lpass=request.form['pwd']
        print(lname,lpass)
        #get details from table and compare both data and direct based on condition.
        cr.execute('SELECT username,password FROM users WHERE username=?',(lname))
        if cr.fetchone():
            credentials=cr.fetchone()
            if credentials[1]==lpass:
                return render_template('ticket.html')
            elif credentials[1]!=lpass:
                return render_template('hold.html')
        else:
            return render_template('hold.html')

#Create Account Creation page direction
@app.route('/c',methods=['GET','POST'])
def create():
    # METHOD to get details for account creation and create the account by storing it to the database.
    if request.method=='POST':
        cname=request.form['name']
        cmail=request.form['mail']
        cphone=request.form['phone']
        cuser=request.form['uname']
        cpass=request.form['pass']
        ccpass=request.form['cpass']
        if cname and cmail and cphone and cuser and cpass and ccpass:    
            if cpass==ccpass:
                #add details to database and redirect to success page
                try:
                    cr.execute('''INSERT INTO users(name,mail,phone,username,password)
                            VALUES(?,?,?,?,?)''',(cname,cmail,cphone,cuser,cpass))
                    base.commit()
                    return render_template('success.html')
                except IntegrityError:
                    return render_template('hold.html')
                except:
                    return 'DATABASE CONNECTION ERROR'
                
            elif cpass != ccpass:
                return render_template('hold.html')
        else:
            return render_template('hold.html')
    return render_template('create.html')
#Run flask object if this document satisfies the main attribute




if __name__=='__main__':
    app.run(debug=True)
