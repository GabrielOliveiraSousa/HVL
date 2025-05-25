import customtkinter as ctk
from datetime import datetime

def TeacherGrades_Window(student_data, ref):
    root = ctk.CTkToplevel()
    root.title("Gerenciamento de Notas")
    root.geometry("600x500")
    root.resizable(False, False)

    grade_vars = []
    weight_vars = []
    
    # Frame principal
    main_frame = ctk.CTkFrame(root)
    main_frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    # Cabeçalho com informações do aluno
    header_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    header_frame.pack(fill="x", pady=(0, 20))

    ctk.CTkLabel(header_frame, text=f"RA: {student_data.get('ra', 'N/A')}", 
                font=('Arial', 14)).grid(row=0, column=0, sticky="w", padx=10)
    
    ctk.CTkLabel(header_frame, text=f"Aluno: {student_data.get('full_name', 'N/A')}", 
                font=('Arial', 16, 'bold')).grid(row=1, column=0, sticky="w", padx=10, pady=5)
    
    ctk.CTkLabel(header_frame, text=f"Curso: {student_data.get('course', 'N/A')}", 
                font=('Arial', 14)).grid(row=2, column=0, sticky="w", padx=10)
    
    # Frame para as notas
    grades_frame = ctk.CTkFrame(main_frame)
    grades_frame.pack(fill="both", expand=True)
    
    # Configuração do grid - 6 colunas no total
    for i in range(6):
        grades_frame.grid_columnconfigure(i, weight=0, minsize=80)

    # Avaliações (agora com 2 colunas por avaliação)
    assessments = [
        {"name": "Prova 1", "row": 0, "col": 0},
        {"name": "Prova 2", "row": 0, "col": 4},
        {"name": "Prova 3", "row": 2, "col": 0},
        {"name": "Prova 4", "row": 2, "col": 4}
    ]

    # Adicionar avaliações
    for assessment in assessments:
        # Nome da avaliação
        ctk.CTkLabel(grades_frame, text=assessment["name"], 
                    font=('Arial', 14, 'bold')).grid(
                    row=assessment["row"], column=assessment["col"], 
                    sticky="w", padx=10)
        
        # Linha de Nota/Peso
        row = assessment["row"] + 1
        
        # Label e Campo Nota
        ctk.CTkLabel(grades_frame, text="Nota:").grid(
            row=row, column=assessment["col"], sticky="e", padx=5)
        
        grade_var = ctk.StringVar(value=str(student_data.get('grades', {}).get(
            assessment["name"].lower().replace(" ", "_"), {}).get('grade', 0)))
        grade_entry = ctk.CTkEntry(grades_frame, textvariable=grade_var, width=60)
        grade_entry.grid(row=row, column=assessment["col"]+1, sticky="w")
        grade_vars.append({"name": assessment["name"], "var": grade_var})
        
        # Label e Campo Peso
        ctk.CTkLabel(grades_frame, text="Peso:").grid(
            row=row, column=assessment["col"]+2, sticky="e", padx=5)
        
        weight_var = ctk.StringVar(value=str(student_data.get('grades', {}).get(
            assessment["name"].lower().replace(" ", "_"), {}).get('weight', 0)))
        weight_entry = ctk.CTkEntry(grades_frame, textvariable=weight_var, width=60)
        weight_entry.grid(row=row, column=assessment["col"]+3, sticky="w")
        weight_vars.append({"name": assessment["name"], "var": weight_var})
    
    # Função para salvar as notas (mantida igual)
    def save_grades():
        try:
            grades_to_save = {}
            for grade in grade_vars:
                name_key = grade["name"].lower().replace(" ", "_")
                grade_value = float(grade["var"].get())
                
                if grade_value < 0 or grade_value > 10:
                    raise ValueError(f"Nota da {grade['name']} deve estar entre 0 e 10")
                
                grades_to_save[name_key] = {
                    "name": grade["name"],
                    "grade": grade_value,
                    "weight": 0
                }
            
            for weight in weight_vars:
                name_key = weight["name"].lower().replace(" ", "_")
                weight_value = float(weight["var"].get())
                
                if weight_value < 0 or weight_value > 100:
                    raise ValueError(f"Peso da {weight['name']} deve estar entre 0 e 100")
                
                grades_to_save[name_key]["weight"] = weight_value
            
            if ref is not None and 'id' in student_data:
                student_ref = ref.child(student_data['id'])
                student_ref.update({"grades": grades_to_save})
                feedback_label.configure(text="Notas salvas com sucesso!", text_color="green")
            else:
                feedback_label.configure(text="Erro: Referência do banco de dados inválida", text_color="red")

        except ValueError as e:
            feedback_label.configure(text=f"Erro: {str(e)}", text_color="red")
        
        root.after(3000, lambda: feedback_label.configure(text=""))
    
    # Frame para botões
    buttons_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
    buttons_frame.pack(pady=20)
    
    # Botão Salvar
    save_button = ctk.CTkButton(
        buttons_frame, 
        text="Salvar Notas", 
        command=save_grades,
        fg_color="#025604",
        hover_color="#027506",
        width=120
    )
    save_button.pack(side="left", padx=10)
    
    # Botão Sair
    exit_button = ctk.CTkButton(
        buttons_frame, 
        text="Sair", 
        command=root.destroy,
        fg_color="#606060",
        hover_color="#777676",
        width=120
    )
    exit_button.pack(side="right", padx=10)
    
    # Feedback
    feedback_label = ctk.CTkLabel(main_frame, text="", height=20)
    feedback_label.pack()
    
    return root

if __name__ == "__main__":
    app = ctk.CTk()
    app.withdraw()
    
    aluno_exemplo = {
        "id": "123",
        "ra": "20230001",
        "full_name": "João da Silva",
        "course": "Engenharia",
        "grades": {
            "prova_1": {"grade": 7.5, "weight": 30},
            "prova_2": {"grade": 8.0, "weight": 30},
            "Prova_3": {"grade": 0, "weight": 0},
            "Prova_4": {"grade": 0, "weight": 0}
        }
    }
    
    TeacherGrades_Window(aluno_exemplo, None)
    app.mainloop()