from flask import *
from sqlite3 import *

app=Flask(__name__)#initiate flask object

base=connect('base.db',check_same_thread=False)
base.execute('''CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            mail TEXT NOT NULL,
            contact INTEGER NOT NULL UNIQUE,
            location TEXT NOT NULL);''')
cr=base.cursor()
#CREATE THE HTML PAGE DIRECT
@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
        uname=request.form['username']
        pwd=request.form['password']
        cr.execute('''SELECT USERNAME,PASSWORD FROM users
        WHERE USERNAME=?''',(uname,))
        var=cr.fetchone()
        if var:
            if var[1]==pwd:
                return render_template('homepage.html')
            elif var[1]!=pwd:
                return render_template('loginfail.html')
        elif not var:
            return render_template('login_page.html')
    return render_template('login_page.html') 

@app.route('/a',methods=['GET','POST'])    
def cre():
    if request.method=='POST':
        aname=request.form['name']
        auname=request.form['username']
        apw=request.form['password']
        acpw=request.form['confirmpassword']
        amid=request.form['mail']
        acon=request.form['contact']
        aloc=request.form['location']
        if aname and amid and acon and auname and apw and acpw:
            if apw==acpw:
                try:
                    cr.execute('''INSERT INTO users(name,username,password,mail,contact,location)
                                VALUES(?,?,?,?,?,?)''',(aname,auname,apw,amid,acon,aloc))
                    base.commit()
                    return render_template('ac_successful_msg.html')
                except IntegrityError:
                    return render_template('ac_failed.html')
            elif apw!=acpw:
                return render_template('ac_failed.html')
            
    return render_template('ac_creation.html')


@app.route('/p',methods=['GET','POST'])
def pg():
    if request.method=='POST':
        objective=dict(request.form)
        print(objective)
        return render_template('result.html',obj=objective)

if __name__=='__main__':
    app.run()


        


#trichy-[0]        FROM CITY
#chennai-[1]       TO CITY
#2022-07-27- [2]   DATE
#divya-[3]         NAME
#235975-[4]        CONTACT
#1-[5]             num of seats
#doubledecker-[14] BUS 
#ac-[15]           SEAT 




