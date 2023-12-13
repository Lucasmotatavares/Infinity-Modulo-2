# Texto = str(input('String Digitada: ')).lower().strip()

def Qtd_Caracteres (String = str):
    Quantidade = len (String)
    return Quantidade

# print(Qtd_Caracteres(Texto))

def Qtd_Consoantes (String = str):
    Qtd_Consoantes = 0
    for Letra in String:
        if Letra in 'bcdfghjklmnpqrstvxywz':
            Qtd_Consoantes += 1
    return Qtd_Consoantes

# print(Qtd_Consoantes(Texto))

def Qtd_Vogais (String = str):
    Qtd_Vogais = 0
    for Letra in String:
        if Letra in 'aeiouáàéèíìóòúù':
            Qtd_Vogais += 1
    return Qtd_Vogais

# print(Qtd_Vogais(Texto))

def Qtd_Vazios (String = str):
    Qtd_Vazios = 0
    for Letra in String:
        if Letra in ' ':
            Qtd_Vazios += 1
    return Qtd_Vazios

# print(Qtd_Vazios(Texto))