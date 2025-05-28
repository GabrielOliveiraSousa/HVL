import customtkinter as ctk
from datetime import datetime

def listStudents_Window(ref):
    global listStudents_root

    #variaveis inexistentes
    #

    def Confirmation():
        name = Name_Input.get()
        birthDate = BirthDate_Input.get()
        student = True
        grade1 = Grade_One.get()
        grade2 = Grade_Two.get()
        grade3 = Grade_Three.get()
        grade4 = Grade_Four.get()
        course = Course_Input.get()

        if validation(name, birthDate):
            newData = {'nwUser': {
                'full_name': name,
                'date_of_birth': birthDate,
                'student': student,
                'grades': {
                    'grade1': grade1,
                    'grade2': grade2,
                    'grade3': grade3,
                    'grade4': grade4,  
                },
                'course': course,
                'RA': RA
                }}
            
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
    
    
    Name_Input = ctk.CTkEntry(CreateUser_root, variable=Name_Input)
    ctk.CTkLabel(CreateUser_root, text='Nome:').pack(pady=10)
    
    BirthDate_Input = ctk.CTkEntry(CreateUser_root, variable=BirthDate_Input).pack(pady=10)
    ctk.CTkLabel(CreateUser_root, text='Data de Aniversário:').pack()
    
    Course_Input = ctk.CTkCTkEntry(CreateUser_root, text='Curso')
    Course_Input.pack(pady=10)
    
    Grade_One = ctk.CTkEntry(CreateUser_root,)
    ctk.CTkLabel(CreateUser_root, text='Data de Aniversário:').pack()
    Grade_One.pack()
     
    Grade_Two = ctk.CTkEntry(CreateUser_root,)
    ctk.CTkLabel(CreateUser_root, text='Data de Aniversário:').pack()
    Grade_Two.pack()
    
    Grade_Three = ctk.CTkEntry(CreateUser_root,)
    ctk.CTkLabel(CreateUser_root, text='Data de Aniversário:').pack()
    Grade_Three.pack()
    
    Grade_Four = ctk.CTkEntry(CreateUser_root,)
    ctk.CTkLabel(CreateUser_root, text='Data de Aniversário:').pack()
    Grade_Four.pack()
    
    RA = ctk.CTkEntry(CreateUser_root,)
    RA.pack()
    

    ButtonContainer_Frame = ctk.CTkFrame(CreateUser_root)
    ButtonContainer_Frame.pack(pady=10)
    ctk.CTkButton(ButtonContainer_Frame, text='Cancelar', fg_color='#606060', command=CreateUser_root.destroy).pack(side='left', padx=5, pady=2)
    ctk.CTkButton(ButtonContainer_Frame, text='Adicionar', fg_color='#025604', hover_color='#027506', command=Confirmation).pack(side='right', padx=5, pady=2)
    
    
    
    return CreateUser_root.result