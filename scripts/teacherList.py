import customtkinter as ctk

def teacherList():
    def closeProgram():
        root.quit()
        root.destroy()

    root = ctk.CTk()
    root.geometry('800x600')
    root.title("aplicação")
    root.protocol("WM_DELETE_WINDOW", closeProgram)
    '''
        ################ LADO ESQUERDO #############################
    '''
    #===frame para informações> RA, nome curso
    info_Container = ctk.CTkFrame(root, fg_color='transparent')
    info_Container.grid(row=0, column=0, pady=10, sticky="w")

    info_Container.columnconfigure(0, minsize=150)
    info_Container.columnconfigure(1, minsize=150)

    ra_label = ctk.CTkLabel(info_Container, text="RA: ")
    ra_label.grid(row=0, column=1, pady=10, sticky="w")

    nome_label = ctk.CTkLabel(info_Container, text="nome: ")
    nome_label.grid(row=1, column=1, pady=10, sticky="w")

    curso_label = ctk.CTkLabel(info_Container, text="curso: ")
    curso_label.grid(row=2, column=1, pady=10, sticky="w")

    #===== frame de outras informações, faltas, presenças etc =====
    frequencia_Container = ctk.CTkFrame(root)
    frequencia_Container.grid(row=1, column=0,padx=10)



    aulas_label = ctk.CTkLabel(frequencia_Container, text="aulas: ")
    aulas_label.grid(row=0, column=1, sticky="w",padx=10)
    aulas_label = ctk.CTkLabel(frequencia_Container, text="0")
    aulas_label.grid(row=0, column=2, sticky="e",padx=10)



    presenca_label = ctk.CTkLabel(frequencia_Container, text="presença: ")
    presenca_label.grid(row=1, column=1, sticky="w",padx=10)
    presenca_num_label = ctk.CTkLabel(frequencia_Container, text="0")
    presenca_num_label.grid(row=1, column=2, sticky="e",padx=10)



    falta_label = ctk.CTkLabel(frequencia_Container, text="faltas: ")
    falta_label.grid(row=2, column=1, sticky="w",padx=10)
    falta_num_label = ctk.CTkLabel(frequencia_Container, text="0")
    falta_num_label.grid(row=2, column=2, sticky="e",padx=10)



    frequencia_label = ctk.CTkLabel(frequencia_Container, text="frequencia: ")
    frequencia_label.grid(row=3, column=1, sticky="w",padx=10)
    frequencia_num_label = ctk.CTkLabel(frequencia_Container, text="0")
    frequencia_num_label.grid(row=3, column=2, sticky="e",padx=10)


    '''
    ################ LADO DIREITO #############################
    '''
    # fim do frame das informações
    #========ScrollableFrame========================
    Output_Frame = ctk.CTkScrollableFrame(root, width=400, height=200, fg_color="#1B1A1E")
    Output_Frame.grid(row=0, column=1, pady=10, sticky="e")

    #====== botões =================
    def btn1_action():
        print("Botão 1 clicado")

    def btn2_action():
        print("Botão 2 clicado")

    def btn3_action():
        print("Botão 3 clicado")

    btn_Container = ctk.CTkFrame(root, fg_color='transparent')
    btn_Container.grid(row=1, column=1, pady=(100,0), sticky="s")
    btn_Container.columnconfigure(0, minsize=150)
    btn_Container.columnconfigure(1, minsize=150)

    btn1 = ctk.CTkButton(btn_Container, text="Botão 1", command=btn1_action)
    btn1.grid(row=0, column=1, pady=10, sticky="s")
    btn2 = ctk.CTkButton(btn_Container, text="Botão 2", command=btn2_action)
    btn2.grid(row=0, column=2, pady=10, sticky="s")
    btn3 = ctk.CTkButton(btn_Container, text="Botão 3", command=btn3_action)
    btn3.grid(row=0, column=3, pady=10, sticky="s")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root.mainloop()
teacherList()