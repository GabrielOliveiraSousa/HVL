import customtkinter as ctk
from scripts.listStudents import listStudents_Window

def teacherHomePage(ConnectedUsed, data, ref):
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    listData = [
        "Nome", "Idade", "Curso", "Nota"
    ]
    
    def boolVerify(val):
        return str(val).strip().lower() == "true"
    
    def listStudents():
        newData = listStudents_Window(ref)
        if not newData or not isinstance(newData, dict):
            return
        if boolVerify(newData["student"]):
            ctk.CTkLabel(Output_Frame, text=newData["full_name"]).grid(row=ListNumber+1, column=0, padx=60, pady=5)
            ctk.CTkLabel(Output_Frame, text=newData["date_of_birth"]).grid(row=ListNumber+1, column=1, padx=30, pady=5)
            ctk.CTkLabel(Output_Frame, text=newData["gender"]).grid(row=ListNumber+1, column=2, padx=30, pady=5)
        # else:
        #     input("no students registered, would you like to register one? y/n ")
        #     if input("y"):
        #         CreateData()
        #     else:
        #         return
            
        

    
    
    def goToStudents():
        btn_listStudents = ctk.CTkButton(root, text="Listar Alunos", command=listStudents, fg_color="#025604", hover_color="#027506", font=('Arial',12))
        btn_send.grid(row=0, column=1, padx=10)
        root.destroy()
        
        
    root = ctk.CTk()
    root.geometry('500x500')
    root.title("Teacher Main Page")
    top_frame = ctk.CTkFrame(root)
    top_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
    top_frame.grid_columnconfigure((0,1,2), weight=1, uniform="a")  # distribuir igualmente

    def btn1_action():
        print("Botão 1 clicado")

    def btn2_action():
        print("Botão 2 clicado")

    def btn3_action():
        print("Botão 3 clicado")

    btn1 = ctk.CTkButton(top_frame, text="Botão 1", command=btn1_action)
    btn2 = ctk.CTkButton(top_frame, text="Botão 2", command=btn2_action)
    btn3 = ctk.CTkButton(top_frame, text="Botão 3", command=btn3_action)

    btn1.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    btn2.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    btn3.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

    # Frame scrollável para a lista de alunos
    list_frame = ctk.CTkScrollableFrame(root, width=560, height=350)
    list_frame.grid(row=1, column=0, padx=20, pady=(0,20), sticky="nsew")

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    
    root.mainloop()
