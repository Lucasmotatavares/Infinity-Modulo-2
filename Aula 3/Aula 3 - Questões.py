# -> Questão Desafio:
Nome = str(input('Digite seu Nome: ')).capitalize()
Sobrenome = str(input('Digite seu Sobrenome: ')).capitalize()
Idade = int(input('Digite sua Idade: '))
Email = str(input('Digite seu E-mail: '))
Aluno = {'Nome': Nome, 'Sobrenome': Sobrenome, 'Idade': Idade, 'Email': Email}
print (f'''
       1 - Nome: {Aluno['Nome']}
       2 - Sobrenome: {Aluno['Sobrenome']}
       3 - Idade: {Aluno['Idade']}
       4 - E-mail: {Aluno['Email']}
''')

Notas = []
Maior_Nota = 0
Menor_Nota = float('inf')
Aprovado = "Reprovado"
for Any in range(4):
    Nota = float(input('Nota: '))
    Notas.append(Nota)
    if Nota > Maior_Nota:
        Maior_Nota = Nota # Maior = max.(Notas)
    if Nota < Menor_Nota:
        Menor_Nota = Nota # Menor = min.(Notas)

Média = sum(Notas)/len(Notas)

if Média >= 7:
    Aprovado = "Aprovado"

Aluno['Média'] = Média

Aluno.update({
    'Nota 1': Notas[0],
    'Nota 2': Notas[1],
    'Nota 3': Notas[2],
    'Nota 4': Notas[3],
    'Maior': Maior_Nota,
    'Menor': Menor_Nota,
    'Situação': Aprovado
})


print (f'''
       1 - Nome: {Aluno['Nome']}
       2 - Sobrenome: {Aluno['Sobrenome']}
       3 - Idade: {Aluno['Idade']}
       4 - E-mail: {Aluno['Email']}
       5 - Média: {Aluno['Média']}
       6 - Nota 1 : {Aluno['Nota 1']}
       7 - Nota 2 : {Aluno['Nota 2']}
       8 - Nota 3 : {Aluno['Nota 3']}
       9 - Nota 4 : {Aluno['Nota 4']}
       10 - Maior Nota : {Aluno['Maior']}
       11 - Menor Nota : {Aluno['Menor']} 
       12 - Situação : {Aluno['Situação']}
''')




