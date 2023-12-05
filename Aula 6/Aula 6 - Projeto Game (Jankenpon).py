import random

Player_Win = 0
Pc_Win = 0
Empates = 0
Lista = ['Pedra', 'Papel', 'Tesoura']

def Jogada_Computador ():
        Escolha = random.choice(Lista)
        return Escolha

while True:

    Pc = Jogada_Computador ()

    Player = str(input('''
                        Opções do Game:
                        Pedra
                        Papel
                        Tesoura
                        Sair
                        Digite sua Opção e Teste sua Sorte! : ''')).capitalize().strip()

    
    if Player == 'Sair':
          print (f'''
                 Placar Final
                 Player {Player_Win} X Pc {Pc_Win} 
                 {Empates} Empates
                 ''')
                # Respostas e Mensagens Geradas podem ser Melhor Acabadas
          break
    elif Player in Lista:
        if Pc == Player:
            Empates += 1
            print (f'''
                    O Player Resultou em {Player}
                    O Pc Resultou em {Pc}
                    O Jogo Terminou em Empate!
                    ''')
            
        elif (Player == 'Pedra' and Pc == 'Tesoura') or (Player == 'Papel' and Pc == 'Pedra') or (Player == 'Tesoura' and Pc == 'Papel'):
                Player_Win += 1
                print (f'''
                    O Player Resultou em {Player}
                    O Pc Resultou em {Pc}
                    O Jogo Terminou, Player foi o Vencedor!
                    ''')
                # Possibilidade de Gerar um Def para Compilar as Condições
        else:
            Pc_Win += 1
            print (f'''
                    O Player Resultou em {Player}
                    O Pc Resultou em {Pc}
                    O Jogo Terminou, Pc foi o Vencedor!
                    ''')
    else:
         print ('''
                Digite uma Escolha Válida
                ''')
