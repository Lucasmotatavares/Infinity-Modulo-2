from tkinter import *

Box = Tk()
Box.title("Nota Bimestral")
Box.geometry("500x500")
Box.configure(bg = "Black")

def Soma():
    Nome = Nome_Aluno.get()
    Nota_1 = float(Nota_1_Aluno.get())
    Nota_2 = float(Nota_2_Aluno.get())
    Soma = (Nota_1 + Nota_2)
    Resultado.configure(text = f"A Soma Bimestral do {Nome} é {Soma}")

Nome_Aluno = Label(text = "Digite o Nome do Aluno: ")
Nome_Aluno.pack()
Nome_Aluno = Entry()
Nome_Aluno.pack()

Nota_1_Aluno = Label(text = "Digite a 1ª Nota: ", background = "Red", foreground = "White", font = ("Arial", 12, "bold", "italic")).pack()
Nota_1_Aluno = Entry()
Nota_1_Aluno.pack()

Nota_2_Aluno = Label(text = "Digite a 2ª Nota: ", bg = "Blue" , fg = "White", font = ("Arial", 12, "bold", "italic")).pack()
Nota_2_Aluno = Entry()
Nota_2_Aluno.pack()

Botão_Resultado = Button(Box, text = "Resultado", command = Soma)
Botão_Resultado.pack()

Resultado = Label(text = "")
Resultado.pack()

Box.mainloop()

# Site Coolers para Buscar Cores Diferenciadas para Usar no Tkinter