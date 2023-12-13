Servidor = {'Lucas': '012.123.123-12'}

while True:
    Operação = int(input('''1 - Adicionar Aluno
2 - Excluir Aluno
3 - Visualizar Banco de Dados
4 - Sair
Digite o Código da Operação Deseja Realizar: '''))
    
    if Operação == 1:
        Aluno = str(input('Aluno: ')).capitalize().strip()
        Matrícula = str(input('Matrícula: ')).strip()
        Servidor.update({Aluno: Matrícula})
    elif Operação == 2:
        Aluno = str(input('Remover Aluno: ')).capitalize().strip()
        if Aluno in Servidor:
            Servidor.pop(Aluno)
            print (f'Aluno {Aluno} Removido do Banco de Dados')
        else:
            print (f'Aluno {Aluno} não Encontrado no Banco de Dados')
            continue
    elif Operação == 3:
        print (Servidor)
    elif Operação == 4:
        break
    else:
        print ('Digite um Código Válido')