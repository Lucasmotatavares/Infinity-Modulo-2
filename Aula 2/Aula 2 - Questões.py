# -> Questão 1:
Lista = [2, 5, 8, 11, 11]
for Number in Lista:
    print (Number**2)

# -> Questão 2:
Países = ("Brasil", "Canadá", "Austrália", "Espanha", "Índia")
for País in Países:
    Caracteres = len(País)
    print (f"{País} Possui {Caracteres} Caracteres")

# -> Questão 3:
# Opção 1:
Lista = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]
for Preço in Lista:
    print (Preço)
Soma = Lista[0][1] + Lista[1][1] + Lista[2][1]
print (f"A Soma dos Produtos é {Soma}")

# Opção 2:
Lista = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]
for Preço in Lista:
    print (Preço)
Soma += Preço[1]
print (f"A Soma dos Produtos é {Soma}")

# -> Questão 4:
Palavras = ["Python", "é", "uma", "Linguagem", "Poderosa"]
for Palavra in Palavras:
    if len(Palavra) > 4:
        print (Palavra)