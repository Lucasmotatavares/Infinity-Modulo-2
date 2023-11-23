# -> Questão Ultimate:
def Imc (Peso:float, Altura:float):
    Imc = Peso / Altura ** 2
    return Imc

Dados_Usuário = []

for Any in range(1, 5):
    Nome = str(input(f'Digite o {Any} Nome: '))
    Peso = float(input(f'Digite o {Any} Peso: '))
    Altura = float(input(f'Digite a {Any} Altura: '))
    Imc_Cálculo = Imc(Peso = Peso, Altura = Altura)
    Dados_Usuário.append({
        'Nome': Nome,
        'Peso': Peso,
        'Altura': Altura,
        'Imc': Imc_Cálculo
        })
    
for Item in Dados_Usuário:
    print (f'''
           Nome: {Item['Nome']}
           Peso: {Item['Peso']}
           Altura: {Item['Altura']}
           Imc: {Item['Imc']:.2f}
           ''')
# Utilização de :.2f tem Função de Reduzir as Casas Decimais

# -> Questão 2:
def Valor_Hora (Salário:float, Horas_Trabalhadas:int):
    Valor_Hora = Salário / Horas_Trabalhadas
    return Valor_Hora

Salário = float(input('Digite Quanto Você Ganha: '))
Horas_Trabalhadas = int(input('Digite Quantas Horas Você Trabalha: '))

print (f'Você Ganha {Valor_Hora(Salário = Salário, Horas_Trabalhadas = Horas_Trabalhadas):.2f}')




