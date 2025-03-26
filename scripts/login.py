
import customtkinter as tk

root = tk.CTk()
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
root.title("aplicação")

# input do email
email_label = tk.CTkLabel(root, text="email", font=('Arial',18), justify="left")
email_label.pack(padx=20)

email_input = tk.CTkTextbox(root, font=('Arial',18), height=50)
email_input.pack(padx=20)

# input da senha
senha_label = tk.CTkLabel(root, text="senha", font=('Arial',18),  justify="left")
senha_label.pack(padx=20)

senha_input = tk.CTkTextbox(root, font=('Arial',18), height=50)
senha_input.pack(padx=20)

# frame dos buttons
buttonframe = tk.CTkFrame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.pack(pady=20)

# button enviar
btn_send = tk.CTkButton(buttonframe, text="enviar")
btn_send.grid(row=0, column=0, sticky=tk.W+tk.E)

# button cancelar
btn_cancel = tk.CTkButton(buttonframe, text="cancelar")
btn_cancel.grid(row=0, column=1, sticky=tk.W+tk.E)

buttonframe.pack()
root.mainloop()
