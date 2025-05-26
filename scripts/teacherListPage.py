import customtkinter as ctk

def teacherList():
  
  def closeProgram():
    root.quit()
    root.destroy()

  root = ctk.CTk()
  root.geometry('800x600')
  root.title("aplicação")
  root.protocol("WM_DELETE_WINDOW", closeProgram)
  root.resizable(width=False, height=False)
  root.columnconfigure(0, minsize=100, weight=0)
  root.columnconfigure(1, minsize=200, weight=1)

  #===frame para informações> RA, nome curso
  info_Container = ctk.CTkFrame(root, fg_color='#2b2b2b')
  info_Container.grid(row=0, column=0, padx=25, pady=25, sticky="nw")

  info_Container.columnconfigure(0, minsize=50)
  info_Container.columnconfigure(1, minsize=100)

  ra_label = ctk.CTkLabel(info_Container, text="RA:")
  ra_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

  ra_label_text =  ctk.CTkLabel(info_Container, text="RA: Nome de teste grande")
  ra_label_text.grid(row=0, column=1, pady=10, padx=10, sticky="w")

  nome_label = ctk.CTkLabel(info_Container, text="Nome:")
  nome_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

  nome_label_text =  ctk.CTkLabel(info_Container, text="RA: Nome de teste grande ")
  nome_label_text.grid(row=1, column=1, pady=10, padx=10, sticky="w")

  curso_label = ctk.CTkLabel(info_Container, text="Curso:")
  curso_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")

  curso_label_text =  ctk.CTkLabel(info_Container, text="RA: Nome de teste grande ")
  curso_label_text.grid(row=2, column=1, pady=10, padx=10, sticky="w")

  #===== frame de outras informações, faltas, presenças etc =====
  frequencia_Container = ctk.CTkFrame(root)
  frequencia_Container.grid(row=2, column=0, padx=25, pady=(150,0), sticky='w')



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

  # fim do frame das informações
  #========ScrollableFrame========================
  Output_Frame = ctk.CTkScrollableFrame(root, width=400, height=200, fg_color="#1B1A1E")
  Output_Frame.grid(row=0, column=1, padx=15, pady=(20,0), sticky="e")
  Output_Frame.columnconfigure(1, weight=3)

  #====== botões =================
  def btn1_action():
    print("Botão 1 clicado")
    btn1.grid_remove()
    btn3.grid()
    btn4.grid()

  def btn2_action():
    print("Voltando")
    root.destroy()

  def btn3_action():
    print("Notas Atualizadas")
    btn3.grid_remove()
    btn4.grid_remove()
    btn1.grid()
    
  def btn4_action():
    print("Cancelando.")
    btn3.grid_remove()
    btn4.grid_remove()
    btn1.grid()

  btn_Container = ctk.CTkFrame(root, fg_color='transparent')
  btn_Container.grid(row=2, column=1, pady=(150,0), sticky="s")
  btn_Container.columnconfigure(0, minsize=150)
  btn_Container.columnconfigure(1, minsize=150)

  btn1 = ctk.CTkButton(btn_Container, text="Atualizar Notas", command=btn1_action)
  btn1.grid(row=0, column=1, pady=10, sticky="s")

  btn2 = ctk.CTkButton(btn_Container, text="Voltar", command=btn2_action)
  btn2.grid(row=0, column=2, pady=10, sticky="s")

  btn3 = ctk.CTkButton(btn_Container, text="Confirmar", command=btn3_action)
  btn3.grid(row=0, column=1, pady=10, sticky="s")

  btn4 = ctk.CTkButton(btn_Container, text="Cancelar", command=btn4_action)
  btn4.grid(row=0, column=2, pady=10, sticky="s")



  btn3.grid_remove()
  btn4.grid_remove()


  ctk.set_appearance_mode("dark")
  ctk.set_default_color_theme("blue")
  root.mainloop()