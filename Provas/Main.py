from Prova import *

Servidor = {}

while True:
    Operation = input('''1 - Adicionar Aluno
2 - Excluir Aluno
3 - Visualizar Banco de Dados
4 - Atualizar Nome de Matrícula
5 - Sair
Digite o Código da Operação Deseja Realizar: ''')

    if Operation == '1':
        print (Adicionar(Servidor))
    elif Operation == '2':
        print (Remover(Servidor))
    elif Operation == '3':
        print (Visualizar(Servidor))
    elif Operation == '4':
        print (Atualizar_Nome(Servidor))
    elif Operation == '5':
        break
    else:
        print ('Digite um Código Válido')

