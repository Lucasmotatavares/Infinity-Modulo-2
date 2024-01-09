from tkinter import *

Caixinha = Tk()
Caixinha.title("Aula 1 - Tk")
Caixinha.geometry("600x400")

def Saudação ():
    Nome = Usuário_Input.get()
    Resultado.configure(text = f"Bem Vindo, {Nome}!")
    print (f"Bem Vindo, {Nome}!")

Usuário_Label = Label(text = "Digite o Nome do Usuário: ") # Pode Colocar .pack() ao Final de um Label que Não Será Configurado!
Usuário_Label.pack()

Usuário_Input = Entry()
Usuário_Input.pack()

Botão_Enviar = Button(Caixinha, text = "Enviar", command = Saudação)
Botão_Enviar.pack()

Resultado = Label(text = "")
Resultado.pack()

Caixinha.mainloop()