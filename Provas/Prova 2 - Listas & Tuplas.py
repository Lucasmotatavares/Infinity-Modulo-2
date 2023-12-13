Lista = []
Pares = []
Impares = []

for Vezes in range(1, 11):
    Number = int(input(f'Digite {Vezes}º Número: '))
    Lista.append(Number)

for Item in Lista:
    if Item % 2 == 0:
        Pares.append(Item)
    elif Item % 2 != 0:
        Impares.append(Item)

print (f'Os Números Pares são {Pares}')
print (f'Os Números Impares são {tuple(Impares)}')
print (f'Quantidade de Pares é {len(Pares)}')
print (f'Quantidade de Impares é {len(Impares)}')
print (f'A Soma dos Números Pares é {sum(Pares)}')
print (f'A Soma dos Números Impares é {sum(Impares)}')
