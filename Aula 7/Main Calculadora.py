# Opção 1:

from Calculadora import *

Lista_Number = []

while True:
    Operação = int(input('''Qual Operação Deseja Realizar?
                            1 - Soma
                            2 - Subtração
                            3 - Multiplicação
                            4 - Divisão
                            5 - Sair
                            '''))
    if Operação == 1:
        while True: 
            Number = float(input()) # Levando em Consideração que Existe uma Interface de Usuário

            Lista_Number.append(Number)

            if Number == 666:
                print (Soma(Lista_Number = Lista_Number))
                break
    elif Operação == 2:
        while True: 
            Number = float(input()) # Levando em Consideração que Existe uma Interface de Usuário

            Lista_Number.append(Number)

            if Number == 666:
                print (Subtração(Lista_Number = Lista_Number))
                break
    elif Operação == 3:
        while True: 
            Number = float(input()) # Levando em Consideração que Existe uma Interface de Usuário

            Lista_Number.append(Number)

            if Number == 666:
                print (Multiplicação(Lista_Number = Lista_Number))
                break
    elif Operação == 4:
        while True: 
            Number = float(input()) # Levando em Consideração que Existe uma Interface de Usuário

            Lista_Number.append(Number)

            if Number == 666: # Não Pode ser 0, Por Isso o 666 # Solução em Transformação de Str em Float?
                print (Divisão(Lista_Number = Lista_Number))
                break

# Opção 2:

from Calculadora import *

Number_1 = float(input("Digite o 1º Número: "))
Number_2 = float(input("Digite o 2º Número: "))

while True:
    Menu = int(input("""
    Escolha uma operação
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    0 - Sair
"""))
    match Menu:
        case 1:
            print (Soma(n1 = Number_1, n2 = Number_2))
        case 2:
            print (Subtração(n1 = Number_1, n2 = Number_2))
        case 3:
            print (Multiplicação(n1 = Number_1, n2 = Number_2))
        case 4:
            print (Divisão(n1 = Number_1, n2 = Number_2))
        case 0:
            break
        case _:
            print("Opção Inválida")
