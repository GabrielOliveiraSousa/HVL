#inicia a conexão com firebase
import firebase_admin
cred_obj = firebase_admin.credentials.Certificate('scripts/serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred_obj, {
  'databaseURL': 'https://hvlgg1-default-rtdb.firebaseio.com/'
})
from firebase_admin import db

#Define o nome do root, e uma "subpasta" chamada usuários
ref = db.reference('pythonFirebaseDbTest/')
user_ref = ref.child("Users")

#Carrega o arquivo JSON dos usuários, contendo dados
import json
with open('scripts/userData.json', "r") as f:
  user_data = json.load(f)

#Pra salvar usuários no banco de dados
for key, value in user_data.items():
  user_ref.push().set(value)
  # if (value["placeholder"] === "placeholder"):
  #     value["placeholder"] = placeholder
  #     ref.child(key).update({"placeholder":placeholder})
  # Esse if pode ser util caso tivermos que adicionar
  # informações a usuários específicos já presentes no BD,
  # talvez através de um botão que chame esse if


#Pra printar no terminal todos os usuarios
ref = db.reference('pythonFirebaseDbTest/Users')
print(ref.order_by_child("full_name").get())

#Pra printar no terminal todo banco de dados
#ref = db.reference('pythonFirebaseDbTest/Users')
#get_Db = ref.get()
#print(get_Db)


# Pra puxar o valor mais alto de determinado atributo
# ref.order_by_child("placeholder").limit_to_last(1).get()

# Pra puxar o valor mais baixo de determinado atributo
# ref.order_by_child("placeholder").limit_to_first(1).get()

# Pra puxar o valor igual a "x" de determinado atributo
# ref.order_by_child("placeholder).equal_to(x).get()

# Pra deletar informações
# for key, value in user_data.items():
  #ref.child(placaholder).set({})