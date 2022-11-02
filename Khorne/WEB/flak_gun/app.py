from flask import *

#app=Flask(__name__)

flak_machine=Flask(__name__)

@flak_machine.route('/')
def index():
    return render_template('index.html')

@flak_machine.route('/nothtml')
def looper():
    return '<h1>this is not html but a string, FLASK !!!!!<>'

@flak_machine.route('/htmlA')
def invoker():
    return render_template('production.html',username='digit')

@flak_machine.route('/htmlB')
def chasm():
    return render_template('ideation.html')

@flak_machine.route('/htmlC')
def maw():
    return render_template('fblogin.html')

#app.run()

if __name__ == '__main__':
    flak_machine.run(debug=True)