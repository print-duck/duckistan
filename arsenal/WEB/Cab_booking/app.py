from flask import *
from sqlite3 import *
app=Flask(__name__)
base=connect('base.db',check_same_thread=False)
base.execute('''CREATE TABLE IF NOT EXISTS users
          (ID INTEGER PRIMARY KEY,
          NAME TEXT NOT NULL,
         USER_NAME TEXT NOT NULL UNIQUE,
         PASSWORD TEXT NOT NULL,
         MAIL TEXT NOT NULL,
         PHONE_NUMBER INTEGER NOT NULL UNIQUE,
         LOCATION TEXT NOT NULL);''' )
cr=base.cursor()         
#create the html page direct
@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
        uname=request.form['username']
        pwd=request.form['password']
        cr.execute('''SELECT USER_NAME,PASSWORD FROM users
        WHERE USER_NAME=?''',(uname,))
        var=cr.fetchone()
        if var:
            if var[1]==pwd:
                return render_template('homepage.html')
            elif var[1]!=pwd:
                return render_template('login_fail.html')
        elif not var:
            return render_template('login_page.html') 


    return render_template('login_page.html')
    #render= raw process and display
@app.route('/a',methods=['GET','POST'])
def cre():
    if request.method=='POST':
        rname=request.form['name']
        ruser=request.form['user']
        rpass=request.form['passw']
        rrpass=request.form['passww']
        rmail=request.form['mail']
        rphn=request.form['phn']
        rloca=request.form['loca']
        if rname and ruser and rpass and rrpass and rmail and rphn and rloca:
            if rpass==rrpass:
                try:
                    cr.execute('''INSERT INTO users
                      (NAME,USER_NAME,PASSWORD,MAIL,PHONE_NUMBER,LOCATION)
                      VALUES(?,?,?,?,?,?)''',(rname,ruser,rpass,rmail,rphn,rloca))
                    base.commit()
                    return render_template('accountsucc.html')
                except IntegrityError:
                    return render_template('account_fail.html')
            elif rpass!=rrpass:
                 return render_template('account_fail.html')

    return render_template('accont_create.html') 

@app.route('/p',methods=['GET','POST'])  
def pg():
    if request.method=='POST':
        object=dict(request.form)
        print(object)
        return render_template('confirm.html',obj=object)

if __name__=='__main__':
    app.run()
#to run the pogram steps:
#step:1 cmd-press tab-app
#step:2  go to-internship-flask-app
#localhost:5000 to run the program





