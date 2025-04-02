import customtkinter as ctk
import time

usersList = ['josh', 'andrew', 'rover']

def Cadastro(authData):

    #criar funções
    def closeProgram():
        if authData is not None:
            authData[0] = {"login":False, "signUp":False, "repeat":False}
            app.result = authData
        app.quit()
        app.destroy()
        

    def finalizar_Cadastro():
        print("cadastro feito")

    def Password_Validation():
        return bool(campo_senha.get()) and campo_senha.get() == campo_confirmacaoSenha.get()

    def process_registration():
        
        nome = campo_nome.get()
        telefone = campo_telefone.get()
        idade = campo_idade.get()
        senha = campo_senha.get()
        genero = cb_genero.get()

        if input_Validation(nome, telefone, idade, senha, genero):
            #verificar se user ja existe
            if nome not in usersList and Password_Validation():
                    finalizar_Cadastro()
                    fb_cadastro.configure(text='Cadastro feito com successo', text_color='green')
                    authData[0] = {"login":False, "signUp":False, "repeat":False}
                    authData[1] = {"name":nome, "age":idade, "telephone":telefone, "password":senha, "gender": genero[0]}
                    app.result = authData
                    time.sleep(1)
                    app.quit()
                    app.destroy()
            elif nome not in usersList and Password_Validation() == False:
                fb_cadastro.configure(text="As senhas digitadas são diferentes.", text_color='red')
            else:
                fb_cadastro.configure(text="Usuário já existente.", text_color='red')
        else:
            fb_cadastro.configure(text="Informações inválidas.", text_color='red')
            
            

    def input_Validation(nome, telefone, idade, senha, genero):
        return all([nome.strip(), telefone.strip(), str(idade).strip(), senha.strip(), genero.strip()])
            

    def goToLogin():
        authData[0] = {"login":True, "signUp":False, "repeat":True}
        app.result = authData
        app.quit()
        app.destroy()


    app = ctk.CTk()
    app.geometry('350x500')
    app.title('Tela de Cadastro')
    app.protocol("WM_DELETE_WINDOW", closeProgram)
    
    # config aparencia
    ctk.set_appearance_mode('dark')

    #title
    ctk.CTkLabel(app, text="Criar Usuário", font=('Arial', 16)).pack(pady=10)

    # container dos input
    InputData_container = ctk.CTkFrame(app, fg_color='transparent')
    InputData_container.columnconfigure(0, minsize=100)
    InputData_container.pack(pady=5, padx=10, fill="both", expand=True)

    #campo nome
    ctk.CTkLabel(InputData_container,text='Nome: ').grid(row=0, column=0, pady=10, sticky="w") # pady = margem
    campo_nome = ctk.CTkEntry(InputData_container,placeholder_text='Digite seu nome', width=200)
    campo_nome.grid(row=0, column=1, pady=10, sticky="w")
    
    #campo telefone
    ctk.CTkLabel(InputData_container, text='Telefone: ').grid(row=1, column=0, pady=10, sticky="w")
    campo_telefone = ctk.CTkEntry(InputData_container,placeholder_text='Digite seu telefone', width=120)
    campo_telefone.grid(row=1, column=1, pady=10, sticky="w")
    
    #campo idade
    ctk.CTkLabel(InputData_container,text='Idade: ').grid(row=2, column=0, pady=10, sticky="w")
    campo_idade = ctk.CTkEntry(InputData_container, width=30)
    campo_idade.grid(row=2, column=1, pady=10, sticky="w")
    
    #campo Genero
    ctk.CTkLabel(InputData_container, text='Gênero: ').grid(row=3, column=0, pady=10, sticky="w")
    cb_genero = ctk.CTkComboBox(InputData_container, values=['Masculino', 'Feminino'])
    cb_genero.grid(row=3, column=1, pady=10, sticky="w")
    
    #campo senha
    ctk.CTkLabel(InputData_container,text='Senha: ').grid(row=4, column=0, pady=10, sticky="w")
    campo_senha = ctk.CTkEntry(InputData_container,placeholder_text='Digite sua senha', show="*")
    campo_senha.grid(row=4, column=1, pady=10, sticky="w")
    
    #campo confirmacao de senha
    ctk.CTkLabel(InputData_container,text='Confirmação: ').grid(row=5, column=0, pady=10, sticky="w")
    campo_confirmacaoSenha = ctk.CTkEntry(InputData_container,placeholder_text='Confirme sua senha', show="*")
    campo_confirmacaoSenha.grid(row=5, column=1, pady=10, sticky="w")

    
    #button cadastro
    btn_cadastro = ctk.CTkButton(app, text="Cadastrar", command=process_registration, corner_radius=32, fg_color="transparent", hover_color="#4158D0", border_color="#FFCC70", border_width=2).pack(pady=25)
    
    ctk.CTkButton(app, text="já tem uma conta", command=goToLogin, fg_color="transparent", hover_color="#4158D0", text_color="white", corner_radius=8).pack()

    #feedback de cadastro
    fb_cadastro = ctk.CTkLabel(app, text='')
    fb_cadastro.pack(pady=5)
    
    
    #start app
    app.mainloop()

    return app.result
