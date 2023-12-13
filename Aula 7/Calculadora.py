# Opção 1:

def Soma (Lista_Number):
    Soma = 0
    for Item in Lista_Number:
        Soma += Item
    return Soma

def Subtração (Lista_Number):
    Subtração = 0
    for Item in Lista_Number:
        Subtração -= Item
    return Subtração

def Multiplicação (Lista_Number):
    Multiplicação = 0
    for Item in Lista_Number:
        Multiplicação *= Item
    return Multiplicação

def Divisão (Lista_Number):
    Divisão = 0
    for Item in Lista_Number:
        if Item == 0:
            return 'Error'
        else: 
            Divisão /= Item
    return Divisão

# Opção 2:

def Soma (Number_1, Number_2):
    return Number_1 + Number_2

def Subtração (Number_1, Number_2):
    return Number_1 - Number_2

def Multiplicação (Number_1, Number_2):
    return Number_1 * Number_2

def Divisão (Number_1, Number_2):
    if Number_2 == 0:
        return "Error"
    else:
        return Number_1 / Number_2