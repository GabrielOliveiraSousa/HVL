from scripts.adminHome import adminHomePage
from scripts.teacherHome import teacherHomePage
from scripts.studentHome import studentHomePage
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
     {"name":"Teste", "age":35, "telephone":"11 123456789", "password":"Teste", "gender": "M", "role":"student"},
    {"name":"aluno", "age":16, "telephone":"11 123456789", "password":"aluno", "gender": "M", "role":"student"},
    {"name":"professor", "age":35, "telephone":"11 123456789", "password":"professor", "gender": "M", "role":"teacher"},
    {"name":"admin", "age":35, "telephone":"11 123456789", "password":"admin", "gender": "M", "role":"admin"}
]

# Open login window
authData = [
    {"login":True, "signUp":False, "repeat":True},
    {"name":'', "age":0, "telephone":'', "password":'', "gender":'', "role":''}
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
'''if user.get('name'):
    teacherHomePage(user, Data, ref)'''
if user.get('role') == "teacher":
    teacherHomePage(user, Data, ref)
elif user.get('role') == "student":
    studentHomePage(user, Data, ref)
elif user.get('role')=="admin":
    adminHomePage(user, Data, ref)
    
    # if user.get('name') and user.get('name') != "nda":