from tkinter import *

Box = Tk()
Box.title("Média Trimestral")
Box.geometry("500x500")

def Média():
    Nome = Nome_Aluno.get()
    Nota_1 = float(Nota_1_Aluno.get())
    Nota_2 = float(Nota_2_Aluno.get())
    Nota_3 = float(Nota_3_Aluno.get())    
    Média = (Nota_1 + Nota_2 + Nota_3)/3

    if Média < 7:
        Resultado.configure(text = f"A Média Trimestral do {Nome} é {Média:.1f}, Reprovado", bg = "Red" , fg = "White", font = ("Arial", 10, "bold", "italic"))
    elif Média >= 7 and Média < 10:
        Resultado.configure(text = f"A Média Trimestral do {Nome} é {Média:.1f}, Aprovado", bg = "Green" , fg = "White", font = ("Arial", 10, "bold", "italic"))
    elif Média == 10:
        Resultado.configure(text = f"A Média Trimestral do {Nome} é {Média:.1f}, Honra ao Mérito", bg = "Blue" , fg = "White", font = ("Arial", 10, "bold", "italic"))
    else:
        Resultado.configure(text = f"A Média {Média:.1f} é Inválida", bg = "Black" , fg = "White", font = ("Arial", 10, "bold", "italic"))     

Nome_Aluno = Label(text = "Digite o Nome do Aluno: ", bg = "#00171F" , fg = "White", font = ("Arial", 10, "bold", "italic"))
Nome_Aluno.pack()
Nome_Aluno = Entry()
Nome_Aluno.pack()

Nota_1_Aluno = Label(text = "Digite a 1ª Nota: ", bg = "#F3DFA2" , fg = "Black", font = ("Arial", 10, "bold", "italic")).pack()
Nota_1_Aluno = Entry()
Nota_1_Aluno.pack()

Nota_2_Aluno = Label(text = "Digite a 2ª Nota: ", bg = "#F3DFA2" , fg = "Black", font = ("Arial", 10, "bold", "italic")).pack()
Nota_2_Aluno = Entry()
Nota_2_Aluno.pack()

Nota_3_Aluno = Label(text = "Digite a 3ª Nota: ", bg = "#F3DFA2" , fg = "Black", font = ("Arial", 10, "bold", "italic")).pack()
Nota_3_Aluno = Entry()
Nota_3_Aluno.pack()

Botão_Resultado = Button(Box, text = "Resultado", command = Média)
Botão_Resultado.pack()

Resultado = Label(text = "")
Resultado.pack()

Box.mainloop()

