# Exercício 1:
# Opção 1:
Cor = str(input("Choose Your Color: ")).capitalize()
if Cor == "Green":
    print ("Go On")
elif Cor == "Yellow":
    print ("Caution")
elif Cor == "Red":
    print == ("Stop")
else:
    print ("Invalid Color, Try Again")

# Opção 2:
Cor = str(input("Choose Your Color: ")).capitalize()
match Cor:
    case "Green":
        print ("Go On")
    case "Yellow":
        print ("Caution")
    case "Red":
        print ("Stop")
    case _: # Atenção ao Uso do Espaço + Underline para Indicar Semelhança ao Else
        print ("Invalid Color, Try Again")

# Opção 3:
Cor = int(input("""Choose Your Color:
                1 - Red
                2 - Yellow
                3 - Green""")) # Uso de Tripla Aspas para Programa Identificar o Enter no Código
match Cor:
    case "3":
        print ("Go On")
    case "2":
        print ("Caution")
    case "1":
        print ("Stop")
    case _:
        print ("Invalid Color, Try Again")

# Exercício 2:
# Opção 1:
Number_1 = int(input("Number 1: "))
Number_2 = int(input("Number 2: "))
Number_3 = int(input("Number 3: "))
if Number_1 != Number_2 and Number_1 != Number_3 and Number_2 != Number_3:
    if Number_1 > Number_2 and Number_1 > Number_3:
        print (f"{Number_1} é o Maior Entre Todos.")
    elif Number_2 > Number_1 and Number_2 > Number_3:
        print (f"{Number_2} é o Maior Entre Todos.")
    elif Number_3 > Number_1 and Number_3 > Number_2:
        print (f"{Number_3} é o Maior Entre Todos.")
elif Number_1 == Number_2 or Number_1 == Number_3 or Number_2 == Number_3:
    print ("Números Iguais Não São Aceitos")

# Questão 1:
Number_1 = int(input("Digite o 1º Número: "))
Number_2 = int(input("Digite o 2º Número: "))
if Number_1 > Number_2:
    print (f"O Maior Número é {Number_1}")
elif Number_2 > Number_1:
    print (f"O Maior Número é {Number_2}")
elif Number_2 == Number_1:
    print ("Números Iguais Inseridos")

# Questão 2:
Number = float(input("What's Your Number? "))
if Number > 0:
    print ("This Number is Positive")
elif Number < 0:
    print ("This Number is Negative")
elif Number == 0:
    print ("This Number is Neutral")

# Questão 3:
# Opção 1: 
Letra = str(input("""Digite seu Sexo:
                 F - Feminino
                 M - Masculino""")).upper().strip()
if len(Letra) == 1:
    if Letra == "F":
        print ("Feminino")
    elif Letra == "M":
        print ("Masculino")
    else:
        print ("Sexo Inválido")
# Opção 2:
Letra = str(input("""Digite seu Sexo:
                 F - Feminino
                 M - Masculino""")).upper().strip()
if len(Letra) == 1:
    match Letra:
        case "F":
            print ("Feminino")
        case "M":
            print ("Masculino")
        case _:
            print ("Sexo Inválido")

# Questão 4:
Nota_1 = float(input("1ª Nota: "))
Nota_2 = float(input("2ª Nota: "))
Nota_3 = float(input("3ª Nota: "))
Nota_4 = float(input("4ª Nota: "))
Média = (Nota_1 + Nota_2 + Nota_3 + Nota_4)/4
if Média == 10:
    print ("Aluno Aprovado com Honra")
elif Média >= 7 and Média < 10:
    print ("Aluno Aprovado")
elif Média < 7 and Média >= 0:
    print ("Aluno Reprovado")
else:
    print ("Dados Inválidos")

# Questão 5:
Letra = str(input("Digite sua Letra: ")).lower()
if len(Letra) == 1:
    if Letra in "aeiou":
        print (f"(A {Letra} é Vogal)")
    elif Letra in "bcdfghjklmnopqrstvxzwy":
        print (f"(A {Letra} é Consoante)")
    else:
        print ("O Caractere Digitado é Inválido")
        
# Questão 6:
# Opção 1:
Number_1 = float(input("1º Number: "))
Number_2 = float(input("2º Number: "))
Resultado = 0
Operation = int(input("""What's Your Operation?
                      1 - Addition
                      2 - Subtraction
                      3 - Multiplication
                      4 - Division
                      : """))

if Operation == 1:
    Resultado = Number_1 + Number_2
elif Operation == 2:
     Resultado = Number_1 - Number_2
elif Operation == 3:
    Resultado = Number_1 * Number_2
elif Operation == 4:
     Resultado = Number_1 / Number_2
else:
    print ("Invalid Operation")

if Resultado % 2 == 0:
    print(f"O {Resultado} é Par")
else:
    print(f"O {Resultado} é Ímpar")

if Resultado > 0:
    print(f"O {Resultado} é Positivo")
elif Resultado < 0:
    print(f"O {Resultado} é Negativo")
else:
    print(f"O {Resultado} é Neutro")

# Opção 2:
Number_1 = float(input("1º Number: "))
Number_2 = float(input("2º Number: "))
Resultado = 0
Operation = int(input("""What's Your Operation?
                      1 - Addition
                      2 - Subtraction
                      3 - Multiplication
                      4 - Division
                      : """))
match Operation:
    case 1:
        Resultado = Number_1 + Number_2
    case 2:
        Resultado = Number_1 - Number_2
    case 3:
        Resultado = Number_1 * Number_2
    case 4:
        Resultado = Number_1 / Number_2
    case _:
        print ("Invalid Choice")

if Resultado % 2 == 0:
    print(f"O {Resultado} é Par")
else:
    print(f"O {Resultado} é Ímpar")

if Resultado > 0:
    print(f"O {Resultado} é Positivo")
elif Resultado < 0:
    print(f"O {Resultado} é Negativo")
else:
    print(f"O {Resultado} é Neutro")

# Questão 7:
Nome = str(input("Digite seu Nome: "))
Contador = 0
for Letra in Nome:
    if Letra.lower() == "a": # Utilizando .lower() Fora da Variável Principal Modificando Apenas Dentro do For
        Contador += 1 # Contador = Contador + 1
print (f"O Nome {Nome} Possui {Contador} Letra(s) A")

# Questão 8:
for Número in range(5, 51):
    print (Número)

# Questão 9:
for Número in range(10, 101):
    if Número  % 3 == 0 and Número % 5 == 0: # Utilizar X % X == 0 para Demonstrar Divisível por X 
        print (Número)

# Questão 10:
Soma = 0
for Valor in range(1, 6):
    Número = float(input(f"Digite o {Valor}º Número: "))
    Soma = Soma + Número
print (f"A Soma dos Números é {Soma}")

# Questão 11:
while True:
    Fruta = str(input("Digite uma Fruta: ")).capitalize()
    if Fruta == "Fim":
        break

# Questão 12:
# Opção 1:
Número = int(input("Digite seu Número: "))
for Info in range(Número, -1, -1):
    print (Info)

# Opção 2:
Número = int(input("Digite seu Número: "))
while Número >= 0:
    print (Número)
    Número -= 1

# Questão 13:
Número = int(input("Digite seu Número: "))
for Tabuada in range(1, 11):
    Resultado = Número * Tabuada
    print(f"{Número} x {Tabuada} = {Resultado}")

# Questão 14:
Frase = str(input("Digite uma Frase: "))
Contador_Vogal = 0
Contador_Consoante = 0

for Letra in Frase:
    if Letra.lower() in "aeiouâáêéîíôóúã":
        Contador_Vogal += 1
    if Letra.lower() in "bcdfghjkmlnpqrstvxywz":
        Contador_Consoante += 1


print(f"A Frase Digitada Possui {Contador_Vogal} Vogais")
print(f"A Frase Digitada Possui {Contador_Consoante} Consoantes")


