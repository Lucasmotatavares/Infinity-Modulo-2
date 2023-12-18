def Adicionar (Servidor):          
    Aluno = str(input('Aluno: ')).capitalize().strip()
    Matrícula = str(input('Matrícula: ')).strip()
    Servidor.update({Matrícula: Aluno})
    return Servidor
    
def Remover (Servidor):
    Matrícula = str(input('Remover Aluno de Matrícula Nº: ')).strip()
    if Matrícula in Servidor:
        Servidor.pop(Matrícula)
        print (f'Aluno {Matrícula} Removido do Banco de Dados')
        return Servidor
    else:
        print (f'Aluno {Matrícula} não Encontrado no Banco de Dados')

def Atualizar_Nome (Servidor):
    Matrícula = str(input('Atualizar Matrícula: ')).strip()
    Novo_Nome = str(input('Novo Nome do Aluno: ')).capitalize().strip()
    if Matrícula in Servidor:
        Servidor[Matrícula] = Novo_Nome
        return Servidor
    
def Visualizar (Servidor):
    for Matrícula, Aluno in Servidor.items():
        return (f'''Aluno: {Aluno} 
Matrícula: {Matrícula}''')
        
