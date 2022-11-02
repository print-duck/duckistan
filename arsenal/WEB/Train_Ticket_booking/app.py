from flask import*
from sqlite3 import*
app=Flask(__name__)
base=connect('base.db',check_same_thread=False)
base.execute('''CREATE TABLE IF NOT EXISTS users
              (ID INTEGER PRIMARY KEY,
              NAME TEXT NOT NULL,
              USERNAME TEXT NOT NULL UNIQUE,
              PASSWORD TEXT NOT NULL,
              MAILID TEXT NOT NULL,
              CONTACTNO INETGER NOT NULL UNIQUE,
              LOCATION TEXT NOT NULL);''')
cr=base.cursor()
#create the html page direct
@app.route('/',methods=['POST','GET']) 
def home(): 
    if request.method=='POST':
        uname=request.form['username']
        lpsw=request.form['password']
        cr.execute('''SELECT USERNAME,PASSWORD FROM users
        WHERE USERNAME=?''',(uname,))
        var=cr.fetchone()
        if var:
            if var[1]==lpsw:
                return render_template('home.html')
            elif var[1]!=lpsw:
                return render_template('loginfail.html')
        elif not var:
            return render_template('login.html')
    return render_template('login.html')

@app.route('/a',methods=['GET','POST'])
def cre():
    if request.method=='POST':
        aname=request.form['name']
        auser=request.form['username']
        apass=request.form['password']
        aconpsw=request.form['confirm password']
        amail=request.form['mailid']
        acontact=request.form['contactno']
        aloc=request.form['location']
        if aname and auser and apass and aconpsw and amail and acontact and aloc:
            if apass==aconpsw:
                try:
                    cr.execute('''INSERT INTO users(NAME,USERNAME,PASSWORD,MAILID,CONTACTNO,LOCATION)
                            VALUES(?,?,?,?,?,?)''',(aname,auser,apass,amail,acontact,aloc))
                    base.commit()
                    return render_template('accdone.html')
                except IntegrityError:
                    return render_template('accfail.html')
            elif apass!=aconpsw:
                return render_template('accfail.html')

                
    return render_template('acc.html')
@app.route('/p',methods=['GET','POST'])
def pg():
    if request.method=='POST':
        object=dict(request.form)
        print(object)
        return render_template('result.html',obj=object)

if  __name__=='__main__':
    app.run()






