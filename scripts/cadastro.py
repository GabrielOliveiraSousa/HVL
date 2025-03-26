from customtkinter import *

app = CTk()
app.geometry('350x700')
app.title('Tela de Cadastro')

# config aparencia
set_appearance_mode('dark')

#criar funções
def validar_cadastro():
    nome = campo_nome.get()
    
    #verificar se user ja existe
    fb_cadastro.configure(text='Cadastro feito com successo', text_color='green')


#campo nome
campo_nome = CTkLabel(app,text='Nome')
campo_nome.pack(pady=10) # pady = margem

campo_nome = CTkEntry(app,placeholder_text='Digite seu nome completo', width=200)
campo_nome.pack(pady=10)

#campo telefone
campo_telefone = CTkLabel(app,text='Telefone')
campo_telefone.pack(pady=10)

campo_telefone = CTkEntry(app,placeholder_text='Digite seu telefone', width=120)
campo_telefone.pack(pady=10)

#campo idade
campo_idade = CTkLabel(app,text='Idade')
campo_idade.pack(pady=10)

campo_idade = CTkEntry(app,width=30)
campo_idade.pack(pady=10)

#campo fumante
ob_fumante = CTkCheckBox(app, text="Fumante", corner_radius=36)
ob_fumante.pack(pady=30)

#campo sexo
campo_sexo = CTkLabel(app, text='Sexo')
campo_sexo.pack(pady=10)

cb_sexo = CTkComboBox(app, values=['Masculino', 'Feminino'])
cb_sexo.pack(pady=10)

#campo senha
campo_senha = CTkLabel(app,text='Senha')
campo_senha.pack(pady=10)

campo_senha = CTkEntry(app,placeholder_text='Digite sua senha', show="*")
campo_senha.pack(pady=10)

#button cadastro
btn_cadastro = CTkButton(app, text="Cadastrar", command=validar_cadastro, corner_radius=32, fg_color="transparent", hover_color="#4158D0", border_color="#FFCC70", border_width=2)
btn_cadastro.pack(pady=25)

#feedback de cadastro
fb_cadastro = CTkLabel(app, text='')
fb_cadastro.pack(pady=5)


#start app
app.mainloop()