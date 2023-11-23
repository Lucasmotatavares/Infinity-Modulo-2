# -> 1: Dicionário
Pessoa = ["Abel", 28, 1.79, 50, True] # A Lista Pode ser Intuitiva para Pensamento Humano, Porém Programa Não Interpreta
print (Pessoa[0]) # Identificar pela Posição
Pessoa_2 = {
    "Nome": "Abel", # 1 Item = Chave: Valor
    "Idade": 28,
    "Altura": 1.79
}
# Dicionário Permite dar Enter na Linha para Melhor Organização
print (Pessoa_2["Nome"]) # Identifica pelo Dicionário

# -> 2: Dicionário (Formas de Codar Dicionário)
# 1ª Forma:
Dicionário = {
    "Módulo": "Python", # Se Repetir Essa Chave, o Programa vai Considerar Apenas a Última Chave
    "Intituição": "Infinity School"
}

# 2ª Forma:
Dicionário = dict( [ ("Módulo", "Python"), ("Instiuição", "Infinity School") ] )

# 3ª Forma:
Dicionário = dict(Módulo = "Python", Instituição = "Infinity School")

# -> 3: Dicionário + Métodos
Dicionário = {
    "Módulo": "Python", 
    "Intituição": "Infinity School"
}
print (list(Dicionário)) # Vai Criar uma Lista Usando as Chaves do Dicionário, os Valores das Chaves são Desconsiderados
print (len(Dicionário)) # Vai Dizer a Quantidade de Chaves de um Dicionário

# -> 4: Exemplo
# Opção 1:
Pessoa = {"Nome": "João", "Idade": 30, "Cpf": "000.000.000-00"} # Verificar Maioridade
if Pessoa["Idade"] >= 18:
    Pessoa["Habilitação"] = True
    print ("João é Maioridade")
    print (Pessoa)
else:
    Pessoa["Nome"] = "Joãozinho"
    print ("João é Pivete")
    print (Pessoa)

# Opção 2:
Pessoa = {"Nome": str(input("Digite seu Nome: ")),
          "Idade": int(input("Digite sua Idade: ")),
          "Cpf": str(input("Digite seu cpf: ")) # Código Regex é Uitilizado para Verificação de Cpf, Número de Telefone, Etc
}
if Pessoa["Idade"] >= 18:
    Pessoa["Habilitação"] = True
    print ("João é Maioridade")
    print (Pessoa)
else:
    Pessoa["Nome"] = "Joãozinho"
    print ("João é Pivete")
    print (Pessoa)

# -> 5: Exemplo
Carro = {"Marca": "Ford", "Modelo": "Ka", "Ano": 2020, "Cor": "Cinza"}
if "Cor" in Carro: # Verifica se Chave Existe no Dicionário e Modifica seu Valor
    Carro["Cor"] = "Preto"
else:
    del Carro["Ano"]
    print (Carro)

# -> 6: Exemplo


# -> 7: Exemplo


# -> 8: Exemplo


# -> 9: Exemplo


# -> 10: Exemplo
