Email = 'Srsirigueijo@hotmail.com'
Senha = 'Gostodedinheiro'
print (f'''Email: {Email}
Senha: {Senha}''')

while True:
    Email_Novo = str(input('Digite o Email Apresentado: '))
    Senha_Nova = str(input('Digite a Senha Apresentada: '))

    if Email_Novo != Email or Senha_Nova != Senha:
        print ('Verifique se o Email ou Senha Digitados são Iguais aos Anteriores')
        continue
    elif Email_Novo == Email and Senha_Nova == Senha:
        print ('Dados Apresentados Corretamente')
        break

