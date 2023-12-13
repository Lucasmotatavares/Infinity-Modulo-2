def Inverter_Texto (Texto:str):
    Texto_Invert = Texto[::-1]
    return Texto_Invert

def Qtd_Palavras (Texto:str):
    Qtd_Palavras = 1
    for Palavra in Texto.strip():
        if Qtd_Palavras == ' ':
            Qtd_Palavras += 1
    return Qtd_Palavras

def Palíndromo (Texto:str):
    Texto_Sem_Espaço = Retirar_Espaço (Texto)
    Texto_Invert = Texto_Sem_Espaço[::-1]
    if Texto_Sem_Espaço == Texto_Invert:
        return 'A Frase Digitada é um Palíndromo'
    else:
        return 'Não é um Palíndromo'
def Retirar_Espaço (Texto:str):
    return Texto.replace(' ', '') # Substitui Elementos