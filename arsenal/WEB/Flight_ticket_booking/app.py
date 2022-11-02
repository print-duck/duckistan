from flask import *
from sqlite3 import *
app=Flask(__name__)
base=connect('base.db',check_same_thread=False)
base.execute('''CREATE TABLE IF NOT EXISTS users
            (ID INTEGER PRIMARY KEY,
            NAME TEXT NOT NULL,
            USERNAME TEXT NOT NULL UNIQUE,
            PASSWORD TEXT NOT NULL,
            MAILID TEXT NOT NULL,
            CONTACT_NO INTEGER NOT NULL UNIQUE,
            LOCATION TEXT NOT NULL);''')
cr=base.cursor()

@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
        luser=request.form['username']
        lpwd=request.form['password']
        cr.execute('''SELECT USERNAME,PASSWORD FROM users
        WHERE USERNAME=?''',(luser,))
        var=cr.fetchone()
        if var:
            if var[1]==lpwd:
                return render_template('home.html')
            elif var[1]!=lpwd:
                return render_template('loginfail.html')
        elif not var:
            return render_template('login.html')
    return render_template('login.html')




@app.route('/a',methods=['GET','POST'])
def cre():
    if request.method=='POST':
        aname=request.form['name']
        auser=request.form['uname']
        apassword=request.form['password']
        aconfrimpass=request.form['cpassword']
        amail=request.form['mail']
        acontact=request.form['contact']
        alocation=request.form['loc']
        if aname and auser and apassword and aconfrimpass and amail and acontact and alocation:
            if apassword==aconfrimpass:
                try:
                    cr.execute('''INSERT INTO users
                    (NAME,USERNAME,PASSWORD,MAILID,CONTACT_NO,LOCATION)
                    VALUES(?,?,?,?,?,?)''',(aname,auser,apassword,amail,acontact,alocation))
                    base.commit()
                    return render_template('accountsucc.html')
                except IntegrityError:
                    return render_template('accountfail.html')
            elif apassword!=aconfrimpass:
                return render_template('accountfail.html')

    return render_template('accountcreation.html')
@app.route('/b',methods=['GET','POST'])
def pg():
    if request.method=='POST':
        object=dict(request.form)
        print(object)
        return render_template('resultpage.html',obj=object)

if __name__=='__main__':
    app.run()


