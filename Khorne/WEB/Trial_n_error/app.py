from flask import *
import sqlite3

db=sqlite3.connect('clients.db', check_same_thread=False)
db.execute('''create table if not exists users
           (id integer primary key,
           username text not null unique,
           name text not null,
           company text not null,
           warehouse int not null,
           location text,
           pass text not null,
           email text unique)''')

cur=db.cursor()
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/s' ,methods=['GET','POST'])
def browse():
    if request.method=='POST':
        l_name=request.form['uname']
        l_pass=request.form['pwd']
        cur.execute('select name from users where name=? and pass=?',(l_name,l_pass))
        credential=cur.fetchone()
        print('GG',l_name,l_pass,credential)
        if credential:
            return render_template('shop.html')
        else:
            return render_template('remind.html')

@app.route('/c')
def cart():
    return render_template("cart.html")        
        
@app.route('/a')
def about():
    return render_template("about.html")

@app.route('/new_acc', methods=['GET','POST'])
def create():
    if request.method=='POST':
        c_name=request.form['name']
        c_company=request.form['company']
        c_wareid=request.form['wareid']
        c_location=request.form['location']
        c_pass=request.form['pass']
        c_cpass=request.form['cpass']
        c_email=request.form['email']
        if c_name and c_company and c_wareid and c_location and c_pass and c_cpass and c_email:
            if c_pass== c_cpass:
                try:
                    db.execute('''insert into users
                            (name,company,warehouse,location,pass,email) 
                            values(?,?,?,?,?,?)''',(c_name,c_company,c_wareid,c_location,c_pass,c_email))
                    db.commit()
                    return render_template('successful.html')
                except sqlite3.IntegrityError:
                    return render_template('remind.html')
            else:
                return render_template('remind.html')
        else:
            return render_template('remind.html')
    return render_template('create.html')

if  __name__=='__main__':
    app.run(debug=True)
