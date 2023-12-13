def Nota_Média (Lista_Notas):
    Média = sum(Lista_Notas) / 4
    return Média

def Verificar_Situação (Média):
    if Média < 7:
        return 'Reprovado'
    elif Média >= 7 and Média < 10:
        return 'Aprovado'
    elif Média == 10:
        return 'Honra ao Mérito'
    else:
        print ('Nota Inválida')

Lista_Notas = []

for Any in range(1, 5):
    Nota = int(input(f'Digite a {Any}ª Nota: '))
    Lista_Notas.append(Nota)

Média = (Nota_Média(Lista_Notas))

print (f'A Nota Média do Aluno é {Nota_Média(Lista_Notas)}')
print (Verificar_Situação(Média))