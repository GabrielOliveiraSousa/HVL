import customtkinter as ctk

def Login(authData, UsersData):    

    def closeProgram():
        if authData is not None:
            authData[0] = {"login":False, "signUp":False, "repeat":False}
            root.result = authData
        root.quit()
        root.destroy()
    # Validação
    def findUser(Username, Password):
        return next((user for user in UsersData if user['name'] == Username and user['password'] == Password), False)

    def VerifyLogin():
        Username = nome_input.get()
        Password = senha_input.get()
        User = findUser(Username, Password)

        if User:
            authData[0] = {"login":False, "signUp":False, "repeat":False}
            authData[1] = User
            root.result = authData
            root.quit()
            root.destroy()
        else: 
            print("usuario ou senha invalido")

    def goToSignUp():
        authData[0] = {"login":False, "signUp":True, "repeat":True}
        root.result = authData
        root.quit()
        root.destroy()

    root = ctk.CTk()
    root.geometry('320x350')
    root.title("aplicação")
    root.protocol("WM_DELETE_WINDOW", closeProgram)

    ctk.CTkLabel(root, text="Conecte-se", font=('arial', 18)).pack(pady=10)

    # input container
    Input_Container = ctk.CTkFrame(root, fg_color='transparent')
    Input_Container.columnconfigure(0, minsize=60)
    Input_Container.columnconfigure(1, minsize=150)
    Input_Container.pack(pady=35, padx=10, fill='both', expand=True)

    # input do email
    ctk.CTkLabel(Input_Container, text="Usuário: ", font=('Arial',12)).grid(row=0, column=0, pady=10, sticky="w")
    nome_input = ctk.CTkEntry(Input_Container, font=('Arial',13), placeholder_text="Digite o seu nome de usuário", width=230)
    nome_input.grid(row=0, column=1, pady=10, sticky="w")

    # input da senha
    ctk.CTkLabel(Input_Container, text="Senha:", font=('Arial',12)).grid(row=1, column=0, pady=10, sticky="w")
    senha_input = ctk.CTkEntry(Input_Container, font=('Arial',13), placeholder_text="Digite a sua senha", width=230)
    senha_input.grid(row=1, column=1, pady=10, sticky="w")
    
    # frame dos buttons
    buttonframe = ctk.CTkFrame(root, fg_color="transparent")
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    buttonframe.pack(pady=10)
    
    # button cancelar
    btn_cancel = ctk.CTkButton(buttonframe, text="cancelar", command=closeProgram, fg_color="#606060", hover_color="#777676", font=('Arial',12))
    btn_cancel.grid(row=0, column=0, padx=10)
    
    # button enviar
    btn_send = ctk.CTkButton(buttonframe, text="enviar", command=VerifyLogin, fg_color="#025604", hover_color="#027506", font=('Arial',12))
    btn_send.grid(row=0, column=1, padx=10)
    
    ctk.CTkButton(root, text="Criar uma conta.", command=goToSignUp, fg_color="transparent", hover_color="#4158D0", text_color="white", corner_radius=8).pack(pady=20)

    root.mainloop()

    return root.result