import customtkinter as ctk
from datetime import datetime

def CreateUser_Window(ref):

    def Confirmation():
        name = Name_Input.get()
        birthDate = BirthDate_Input.get()
        getGender = Gender_Input.get()
        gender = getGender[0]

        if validation(name, birthDate):
            newData = {
                "nwUser": {
                    "full_name": name,
                    "date_of_birth": birthDate,
                    "role": "student",
                    "gender": gender}}
            for key, value in newData.items():
                ref.push().set(newData["nwUser"])
            CreateUser_root.result = newData
            CreateUser_root.quit()
            CreateUser_root.destroy()

        
    def validation(nome, birthdate):
        try:
            datetime.strptime(birthdate, "%B %d, %Y")
            return bool(nome.strip())
        except ValueError:
            return False
    
    global CreateUser_root
    CreateUser_root = ctk.CTkToplevel()
    CreateUser_root.result = None    
    CreateUser_root.attributes('-topmost', True)
    CreateUser_root.focus_force()
    CreateUser_root.geometry('300x350')
    CreateUser_root.title("Criar Usuário")


    Checkbox_Value = ctk.BooleanVar(value=False)


    ctk.CTkLabel(CreateUser_root, text="Criar Usuário", font=('Arial', 16)).pack(pady=10)

    # Name Entry
    ctk.CTkLabel(CreateUser_root, text="Nome:").pack()
    Name_Input = ctk.CTkEntry(CreateUser_root, width=200)
    Name_Input.pack(pady=5)

    # Birth Entry
    ctk.CTkLabel(CreateUser_root, text="Nascimento:").pack()
    BirthDate_Input = ctk.CTkEntry(CreateUser_root, width=200)
    BirthDate_Input.pack(pady=5)

    #campo Genero
    ctk.CTkLabel(CreateUser_root, text='Gênero: ').pack()
    Gender_Input = ctk.CTkComboBox(CreateUser_root, values=['Masculino', 'Feminino'])
    Gender_Input.pack(pady=5)
    

    Student_Checkbox = ctk.CTkCheckBox(CreateUser_root,
                                       text="Estudante",
                                       variable=Checkbox_Value,
                                       onvalue=True,
                                       offvalue=False
    )
    Student_Checkbox.pack(pady=10)

    # Button Container
    ButtonContainer_Frame = ctk.CTkFrame(CreateUser_root)
    ButtonContainer_Frame.pack(pady=10)

    ctk.CTkButton(ButtonContainer_Frame, text="Cancelar", fg_color="#606060", command=CreateUser_root.destroy).pack(side="left", padx=5, pady=2)
    ctk.CTkButton(ButtonContainer_Frame, text="Adicionar", fg_color="#025604", hover_color="#027506", command=Confirmation).pack(side="right", padx=5, pady=2)

    return CreateUser_root.result
