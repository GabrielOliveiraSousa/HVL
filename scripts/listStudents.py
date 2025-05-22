import customtkinter as ctk
from datetime import datetime

def listStudents_Window(ref):
    global listStudents_root

    def Confirmation():
        name = Name_Input.get()
        birthDate = BirthDate_Input.get()
        student = Checkbox_Value.get()
        if validation(name, birthDate):
            newData = {'nwUser': {'full_name': name, 'date_of_birth': birthDate, 'student': student, 'grade': grade}}
            for key, value in newData.items():
                ref.push().set(newData['nwUser'])
            CreateUser_root.result = newData
            CreateUser_root.quit()
            CreateUser_root.destroy()

    def validation(nome, birthdate):
        try:
            datetime.strptime(birthdate, '%B %d, %Y')
            return bool(nome.strip())
        except ValueError:
            return False
        else:
            pass
          
          
    CreateUser_root = ctk.CTkToplevel()
    CreateUser_root.result = None
    CreateUser_root.attributes('-topmost', True)
    CreateUser_root.focus_force()
    CreateUser_root.geometry('300x350')
    CreateUser_root.title('Lista de Alunos')
    
    
    BirthDate_Input = ctk.BooleanVar(value=False)
    ctk.CTkLabel(CreateUser_root, text='Adicionar Aluno', font=('Arial', 16)).pack(pady=10)
    
    ctk.CTkLabel(CreateUser_root, text='Nome:').pack()
    Gender_Input = ctk.CTkEntry(CreateUser_root, width=200)
    Gender_Input.pack(pady=5)
    
    ctk.CTkLabel(CreateUser_root, text='Nascimento:').pack()
    ref = ctk.CTkEntry(CreateUser_root, width=200)
    ref.pack(pady=5)
    
    Class_Checkbox = ctk.CTkCheckBox(CreateUser_root, text='Estudante', variable=BirthDate_Input, onvalue=True, offvalue=False)
    Class_Checkbox.pack(pady=10)
    
    
    ButtonContainer_Frame = ctk.CTkFrame(CreateUser_root)
    ButtonContainer_Frame.pack(pady=10)
    ctk.CTkButton(ButtonContainer_Frame, text='Cancelar', fg_color='#606060', command=CreateUser_root.destroy).pack(side='left', padx=5, pady=2)
    ctk.CTkButton(ButtonContainer_Frame, text='Adicionar', fg_color='#025604', hover_color='#027506', command=Confirmation).pack(side='right', padx=5, pady=2)
    return CreateUser_root.result