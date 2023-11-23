# -> 1: Listas
Variável = 0
Lista_1 = ["Abel", "João"] # Strings na Lista
Lista_2 = ["Abel", 25] # Strings + Inteiros
Lista_3 = ["Abel", 28, 28.5, True, Variável]
Lista_4 = ["Abel", 28, 28.5, True, Variável, [1, 2, "Abel"]] # Possibilidade de Listas Dentro de Listas
print (Lista_1[1]) # Executa a Informação no Lugar Específico na Lista na Ordem Crescente de 0 a X
print (Lista_4[-2]) # Executa a Informação no Lugar Específico na Lista na Ordem Decrescente de -1 a -X
print (Lista_4[5][2]) # Executa o Índice da Lista Dentro de Lista
print (len(Lista_4))
print (Lista_4[len(Lista_4) - 2]) # Executa a Informação no Lugar Específico na Lista na Ordem Decrescente no Modo Raíz
# print (Lista_4[len(Lista_4) - 2]) = print (Lista_4[-2])

# -> 2: Exemplo
Lista = ["Texto", 25, True, 1.4, "Texto 2"]
print (Lista[1] + 10)

# -> 3: Transformar Info da Lista
Lista = ["Maria", 25, 1.58, ["Maçã", "Banana", "Uva"], "Solteira"]
Lista[3][1] = "Melancia" # Transforma Índice Específico na Lista
Lista[0] = [3, 5] # Transforma Varável Simples em Lista
# Isso Pode Usado em Troca de Type Forçadamente
print (Lista)

# -> 4: Adicionar Itens na Lista
# Opção 1:
Lista = ["Uva", "Pêra", "Melão"]
Quantidade = int(input("Quantas Frutas quer Adicionar? : "))
for Info in range(Quantidade):
    Fruta = str(input("Digite uma Fruta: "))
    Lista.append(Fruta)
print (Lista)

# Opção 2:
Lista = []
Quantidade = int(input("Quantas Frutas Serão Inserir? : "))
while len(Lista) < Quantidade:
    Lista.append(str(input("Digite uma Fruta: ")))
print (Lista)

# -> 5: Exclusão de Índices na Lista
Frutas = ["Uva", "Pêra", "Melão"]
Excluídos = [] # Pode Remover Também sem Necessidade de Armazenar em Uma Lista
# Criar as Listas Respectivas para Armazenar os Dados
Fruta_Excluída = Frutas.pop(1)
Excluídos.append(Fruta_Excluída)
# Utilizar Pop na Lista Desejada e Armazenar na Lista Desejada
print(Frutas)
print(Excluídos)

#  -> 6: Exemplo
Frutas = ["Uva", "Pêra", "Melão", "Maça", "Banana", "Acerola", "Abacaxi"]
print (Frutas)
Posição = int(input("Digite a Posição da Fruta que Deseja Excluir: "))
Frutas.pop(Posição - 1)
print (Frutas)

# -> 7: Exemplo
# Intenção de Remover o Último ou Escolher a Posição
# Opção 1:
Frutas = ["Uva", "Pêra", "Melão", "Maça", "Banana", "Acerola", "Abacaxi"]
while True:
    Menu = int(input("""Qual Operação Deseja Executar?
                 1 - Excluir a Última Fruta
                 2 - Excluir por Posição
                 0 - Sair
                 """))
    match Menu:
        case 1:
            Frutas.pop()
        case 2:
            Posição = int(input("Qual Posição Deseja Excluir? "))
            Frutas.pop(Posição - 1)
        case 0:
            break
        case _:
            print ("Opção Inválida")

# Opção 2:
Frutas = ["Uva", "Pêra", "Melão", "Maça", "Banana", "Acerola", "Abacaxi"]
while True:
    Menu = int(input("""Qual Operação Deseja Executar?
                 1 - Excluir a Última Fruta
                 2 - Excluir por Posição
                 0 - Sair
                 """))
    if Menu == 1:
        Frutas.pop()
    elif Menu == 2:
        print(Frutas)
        Posição = int(input("Qual Posição Deseja Excluir? "))
        Frutas.pop(Posição - 1)
    elif Menu == 0:
        break
    else:
        print("Opção Inválida")

# -> 8: Utilização de Sort
Frutas = ["Uva", "Pêra", "Melão", "Maça", "Banana", "Acerola", "Abacaxi"]
Frutas.sort() # Ordena por Ordem Crescente ou por Ordem Alfabética
print (Frutas)
# Não Ordena Types Diferentes

# -> 9: Utilização de Reverse

Frutas = ["Uva", "Pêra", "Melão", "Maça", "Banana", "Acerola", "Abacaxi"]
Frutas.reverse() # Ordena por Ordem Decrescente ou por Ordem Não-Alfabética
print (Frutas)
# Não Ordena Types Diferentes

# -> 10: Utilização de Index
Frutas = ["Uva", "Pêra", "Melão", "Maça", "Banana", "Acerola", "Abacaxi"]
Posição = Frutas.index("Pêra") # Identifica a Poisção do Item na Lista
print (Posição)

# -> 11: Utilização do Count
Frutas = ["Uva", "Pêra", "Melão", "Maça", "Banana", "Acerola", "Abacaxi", "Uva"]
Quantidade = Frutas.count("Uva") # Faz a Contagem de uma Info Dentro da Lista
print (Quantidade)

# -> 12: Tuplas
# Tupla é Nada Mais que Uma Lista Imutável, Exemplo de Alfabeto que não Precisa de Modificações
Lista = [1, 2, 3, 4, 5] # Utilização de Colchetes
Tupla = (1, 2, 3, 4, 5) # Utilização de Parênteses

# -> 13: Iteração de Listas
Frutas = ["Uva", "Pêra", "Melão", "Uva", "Maça", "Banana", "Acerola", "Abacaxi", "Uva"]
for Fruta in Frutas:
    if Fruta == "Uva":
        print ("Achei uma Uva")
