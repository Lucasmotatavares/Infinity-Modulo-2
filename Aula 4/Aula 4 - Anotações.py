# -> 1: Funções
print ("Alguma Coisa")
input ("Escreva Algo: ")
# São Funções do Python Nativas

# -> 2: Exemplo
def Saudação (Nome): # Definiu a Sintaxe para Receber (Variável)
    print (f"Olá {Nome}") # Ao Receber a Variável Executa o Programado
Saudação ('Lucas')

# -> 3: Exemplo
def Somar (N1, N2):
    return N1 + N2 # Guarda a Informação em Vez de Executar
Resultado = Somar (5,8)
Média = Resultado / 2
print (Média)

# -> 4: Exemplo
def Checar_Nota (Nota):
  if Nota >=0 and Nota <= 10:
    return "Válido"
  else:
    return "Inválido"
  
print (Checar_Nota(5))
print (Checar_Nota(-5))
print (Checar_Nota(50))
print (Checar_Nota(9))

# -> 5: Exercício
# Parte 1:
def Checar_Horário (Horário): # Variável Horário é Restrita à Sintaxe
    if Horário >= 5 and Horário <= 12:
        return 'Bom Dia'
    elif Horário > 12 and Horário <= 18:
        return 'Boa Tarde'
    else:
        return 'Boa Noite'
print (Checar_Horário(6))
print (Checar_Horário(15))
print (Checar_Horário(23))

# Parte 2:
Horário = int(input('Digite que Horas São: '))
print (Checar_Horário(Horário)) # Não Confundir Variável Horário da Sintaxe em Laranja com Varável do Usuário em Branco
Horário_Futuro = int(input('Digite que Horas São: '))
print (Checar_Horário(Horário + 2))

# -> 6: Exercício
# Opção 1:
def Maior (N1, N2, N3):
    if N1 != N2 != N3: # Pode Usar >= e <= para Evitar If Dentro de If 
        if N1 > N2 and N1 > N3:
            return f'O {N1} é o Maior Número'
        elif N2 > N1 and N2 > N3:
            return f'O {N2} é o Maior Número'
        elif N3 > N1 and N3 > N2:
            return f'O {N3} é o Maior Número'
    else:
        return 'Os Números Precisam ser Difirentes'
    
Número_1: int(input('Digite o 1º Número: '))
Número_2: int(input('Digite o 2º Número: '))
Número_3: int(input('Digite o 3º Número: '))

print (Maior(Número_1, Número_2, Número_3))

# Opção 2:
def Maior (N1, N2, N3):
    if N1 != N2 != N3: # Pode Usar >= e <= para Evitar If Dentro de If 
        if N1 > N2 and N1 > N3:
            return f'O {N1} é o Maior Número'
        elif N2 > N1 and N2 > N3:
            return f'O {N2} é o Maior Número'
        elif N3 > N1 and N3 > N2:
            return f'O {N3} é o Maior Número'
    else:
        return 'Os Números Precisam ser Difirentes'
Lista = []
for Any in range(1,4):
    Número = int(input(f'Digite o {Any}º Número: '))
    Lista.append(Número)

print (Maior(Lista[0], Lista[1], Lista[2]))

# Opção 3:
def Maior (Lista):
    Maior_Número = 0
    for Número in Lista:
        if Número > Maior_Número:
            Maior_Número = Número
    if Maior_Número == 0:
        return "Digite Números Positivos"
    else:
        return Maior_Número
Lista = []
for Any in range(1,4):
    Número = int(input(f'Digite o {Any}º Número: '))
    Lista.append(Número)

print (Maior(Lista))

# -> 7: Exemplo
# Programação Organizada para Fácil Entendimento de Terceiros
def Saudação (Nome:str, Hora:int): # Dá ao Usuário Dicas Sobre o que o Programa se Refere
  if Hora >= 5 and Hora <= 12:
    return f"bom dia {Nome}"
  elif Hora > 12 and Hora <= 18:
    return f"boa tarde {Nome}"
  else:
    return f"boa noite {Nome}"
  

print (Saudação(Hora = 18, Nome = "Abel")) # Se Refere às Informações Acima

# -> 8: Extra
from datetime import datetime
# Forma de Recuperar Informação de datas, Horas, Minutos Etc, Nativo do Python
print(f"{datetime.now().hour}:{datetime.now().minute}")