from scripts.home import HomePage
from scripts.cadastro import Cadastro
from scripts.login import Login
import firebase_admin
from firebase_admin import db
cred_obj = firebase_admin.credentials.Certificate('scripts/serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://hvlgg1-default-rtdb.firebaseio.com/'
})


ref = db.reference('pythonFirebaseDbTest/Users')
Data = ref.get()

UsersData = [
    {"name":"Teste", "age":35, "telephone":"11 123456789", "password":"Teste", "gender": "M"},
    {"name":"James159", "age":23, "telephone":"22 546787945", "password":"15961a", "gender": "M"}
]

# Open login window
authData = [
    {"login":True, "signUp":False, "repeat":True},
    {"name":'', "age":0, "telephone":'', "password":'', "gender":''}
]

def Connect(authData): 
    authProcess = {"login":True, "signUp":False, "repeat":True}
    
    
    while authProcess["repeat"]:
        if authProcess["login"]:
            authData = Login(authData, UsersData)
            authProcess = authData[0]
        elif authProcess["signUp"]:
            authData = Cadastro(authData)
            authProcess = authData[0]
        else: 
            authData['repeat'] = False
    return authData[1]

user = Connect(authData)

# Open the homepage 
if user.get('name') and user.get('name') != "nda":
    HomePage(user, Data, ref)