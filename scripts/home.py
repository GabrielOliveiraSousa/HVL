import customtkinter as ctk
from scripts.createUser import CreateUser_Window


def HomePage(ConnectedUser, data, ref):

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Variables
    ListHeader_List = [
        "Nome", "Idade", "Gênero", "Aluno"
    ]

    # Functions
    
    def boolVerify(val):
        return str(val).strip().lower() == "true"

    def AddItem(start, listCounter, data):
        global ListNumber
        
        column_Value = 0
        for item in ListHeader_List:
            ctk.CTkLabel(Output_Frame, text=item, font=('Arial', 14, "bold")).grid(row=0, column=column_Value, padx=10, pady=5)
            column_Value += 1
            listCounter += 1

        for r, user in enumerate(data.values() if isinstance(data, dict) else data, start=start):
            ctk.CTkLabel(Output_Frame, text=user["full_name"]).grid(row=r, column=0, padx=60, pady=5)
            ctk.CTkLabel(Output_Frame, text=user["date_of_birth"]).grid(row=r, column=1, padx=30, pady=5)
            ctk.CTkLabel(Output_Frame, text=user["gender"]).grid(row=r, column=2, padx=30, pady=5)

            if boolVerify(user["student"]): 
                student_Value = "Sim"
                color_Value = "#00ff00"
            else: 
                student_Value = "Não"
                color_Value = "red"

            ctk.CTkLabel(Output_Frame, text=student_Value, text_color=color_Value, ).grid(row=r, column=3, padx=20, pady=5, sticky="e")
            listCounter+=1

        ListNumber = listCounter 
        return listCounter

    def CreateData():
        global ListNumbers

        newData = CreateUser_Window(ref)
        if not newData or not isinstance(newData, dict):
            return 

        ctk.CTkLabel(Output_Frame, text=newData["full_name"]).grid(row=ListNumber+1, column=0, padx=60, pady=5)
        ctk.CTkLabel(Output_Frame, text=newData["date_of_birth"]).grid(row=ListNumber+1, column=1, padx=30, pady=5)
        ctk.CTkLabel(Output_Frame, text=newData["gender"]).grid(row=ListNumber+1, column=2, padx=30, pady=5)

        if boolVerify(newData["student"]): 
            student_Value = "Sim"
            color_Value = "#00ff00"
        else: 
            student_Value = "Não"
            color_Value = "red"

        ctk.CTkLabel(Output_Frame, text=student_Value, text_color=color_Value, ).grid(row=ListNumber+1, column=3, padx=20, pady=5, sticky="e")


    root = ctk.CTk()
    root.geometry('500x500')
    root.title("Main Page")

    Header_container = ctk.CTkFrame(root)
    ctk.CTkLabel(root, text=f"Olá {ConnectedUser['name']}", font=('Arial', 19)).pack(anchor="w", padx=10, pady=25)

    # Create User Button
    CreateUser_Button = ctk.CTkButton(root, text="Criar Usuário", command=CreateData)
    CreateUser_Button.pack(pady=5, padx=10)


    Output_Frame = ctk.CTkScrollableFrame(root, width=450, height=200, fg_color="#1B1A1E")
    Output_Frame.pack(pady=10,padx=10, fill="both", expand=True)

    ListNumber = 0

    ListNumber = AddItem(1, ListNumber, data)


    # Users TreeView
    root.mainloop()
