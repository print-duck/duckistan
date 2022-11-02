import pyrebase
#print(dir(pyrebase))
#Get these config data from Project Overview in firebase
config={
  'apiKey': "AIzaSyC0hbVEOh1c1dApYWuqW-14tccJWBkIAVo",
  'authDomain': "enigma-9e9a9.firebaseapp.com",
  'databaseURL': "https://enigma-9e9a9-default-rtdb.firebaseio.com",
  'projectId': "enigma-9e9a9",
  'storageBucket': "enigma-9e9a9.appspot.com",
  'messagingSenderId': "808789461103",
  'appId': "1:808789461103:web:f1d6f9cfeda5068835e59a",
  'measurementId': "G-MB1404TLQX"
}

#initialize a pyrebase object
firebase = pyrebase.initialize_app(config)
#initialize a database object
fdb = firebase.database()
#print(dir(fdb))

#now to upload data to the base
data={'Hello world':{'project_name':'Tzeentch','goal':'Ascension','pressure':0,'agenda':False,'skill':'100','luck':0}}

#data={100:'ONE HUNDREDDD'}

fdb.set(data)
