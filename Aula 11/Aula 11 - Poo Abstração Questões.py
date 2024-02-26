# -> Exercício 1:

class Celular:
    def __init__(self, Marca:str, Modelo:str, Cor:str, Ano:int, Armazenamento:int) -> None: # Pode Remover "-> None", Significa que a Função Retornará Nada
        # É de Bom Costume Codar os Mesmos Names no "Self" e nas Variáveis
        self.Brand = Marca
        self.Model = Modelo
        self.Color = Cor
        self.Year = Ano
        self.Storage = Armazenamento

Celular_1 = Celular(Marca = "Samsung", Modelo = "S22 Ultra", Cor = "Cinza", Ano = 2022, Armazenamento = 256)
Celular_2 = Celular('Apple', 'Iphone 15', 'Preto', 2023, 512)
# Caso Saiba a Ordem das Características, Não Precisa Determinar as Variáveis Respectivas, Porém Não é Recomendado
Celular_3 = Celular(Modelo = 'S23', Armazenamento = 512, Marca = 'Samsung', Cor = 'Branco', Ano = 2023)

Marca_Celular = str(input('Digite a Marca do Celular: '))
Modelo_Celular = str(input('Digite a Modelo do Celular: '))
Cor_Celular = str(input('Digite a Cor do Celular: '))
Ano_Celular = int(input('Digite a Ano do Celular: '))
Armazenamento_Celular = int(input('Digite a Armazenamento do Celular: '))

Celular_4 = Celular(Marca = Marca_Celular, Modelo = Modelo_Celular, Cor = Cor_Celular, Ano = Ano_Celular, Armazenamento = Armazenamento_Celular)

print (Celular_1.Model, Celular_1.Storage)
print (Celular_2.Color, Celular_2.Year)
print (Celular_3.Brand, Celular_3.Model)
print (f'O Celular {Celular_1.Model} tem {Celular_1.Storage} de Armazenamento')
print (Celular_4)

# -> Exercício 2:

class Car:
    def __init__(self, Brand:str, Model:str, Color:str, Year:int, Doors:int,  Air_System:bool, Auto_Glass:bool):
        self.Brand = Brand
        self.Model = Model
        self.Color = Color
        self.Year = Year
        self.Doors = Doors
        self.Air_System = Air_System
        self.Auto_Glass = Auto_Glass

Brand = str(input('Car Brand = '))
Model = str(input(' Car Model = '))
Color = str(input(' Car Color = '))
Year = int(input(' Car Year = '))
Doors = int(input(' Car Doors = '))
Air_System = bool(input(' Car Air System = '))
Auto_Glass = bool(input(' Car Auto Glass = '))
# Dodge, Challenger 6.2, Orange, 1970, 2, False, False

Car_1 = Car(Brand = 'Wolkswagen', Model = 'Gol GTI 2.0', Color = 'Preto', Year = 1989, Doors = 2, Air_System = True, Auto_Glass = True)
Car_2 = Car(Brand = 'Ford', Model = 'Maverick Supercharger', Color = 'Azul', Year = 1979, Doors = 2, Air_System = False, Auto_Glass = False)
Car_3 = Car(Brand = Brand, Model = Model, Color = Color, Year = Year, Doors = Doors, Air_System = Air_System, Auto_Glass = Auto_Glass)

# Está com Problema no Print do Car_3, nas Variáveis Booleanas
print (Car_1.Brand, Car_1.Model)

print (Car_2.Model, Car_2.Year)
if Car_2.Auto_Glass:
    print ('Auto Glass: Check')
else:
    print ('Auto Glass: Uncheck')

print (f'''
       Car Brand: {Car_3.Brand} 
       Model: {Car_3.Model} 
       Color: {Car_3.Color} 
       Year: {Car_3.Year}, 
       {Car_3.Doors} Doors,
''')

if Car_3.Air_System:
    print ('Air System: Check')
else:
    print ('Air System: Uncheck')
if Car_3.Auto_Glass:
    print ('Auto Glass: Check')
else:
    print ('Auto Glass: Uncheck') 

# -> Exercício 3:

class Celular:
    def __init__(self, Marca:str, Modelo:str, Cor:str, Ano:int, Armazenamento:int):
        self.Brand = Marca
        self.Model = Modelo
        self.Color = Cor
        self.Year = Ano
        self.Storage = Armazenamento

    def Ligação (self, Número):
        return f"O Celular {self.Model} Está Fazendo uma Ligação para o Número {Número}"

    def Desligar (self):
        return f"O Celular {self.Model} está Desligando"

    def Info (self):
        return f'''
Marca: {self.Brand}
Modelo: {self.Model}
Cor: {self.Color}
Ano: {self.Year}
Armazenamento: {self.Storage}
'''

Celular_1 = Celular(Marca = "Samsung", Modelo = "S23 Plus", Cor = "Prata", Ano = 2023, Armazenamento = 512)

print (Celular_1.Desligar())

Número_Celular = str(input("Digite o Número do Celular: "))
print (Celular_1.Ligação(Número = Número_Celular))
print (Celular_1.Ligação(Número = "(82) 98521-1464"))
print (Celular_1.Ligação(Número = "(11) 98943-3647"))

print (Celular_1.Info())

# -> Questão 1:

class Dog:
    def __init__(self, Name:str, Race:str, Years:int):
        self.Name = Name
        self.Race = Race
        self.Years = Years

Doggy = Dog(Name = "Smeagol", Race = "Dachshund", Years = 2)


Name_Dog = str(input("Digite o Nome do Dog: "))
Race_Dog = str(input("Digite a Raça do Dog: "))
Years_Dog = int(input("Digite a Idade do Dog: "))

Doggy_2 = Dog(Name = Name_Dog, Race = Race_Dog, Years = Years_Dog)


print (f"Meu Dog se Chama {Doggy.Name}, é da Raça {Doggy.Race} e tem {Doggy.Years} Anos")

# -> Questão 2:

class Pessoa:
    def __init__(self, Nome:str, Idade:int, Peso:float, Gênero:str):
        self.Nome = Nome
        self.Idade = Idade
        self.Peso = Peso
        self.Gênero = Gênero

Indivíduo = Pessoa(Nome = 'Lucas', Idade = 28, Peso = 75, Gênero = 'Menines')

Nome_Pessoa = str(input('Digite seu Nome: '))
Idade_Pessoa = int(input('Digite sua Idade: '))
Peso_Pessoa = float(input('Digite seu Peso: '))
Gênero_Pessoa = str(input('Digite seu Gênero: '))

Indivíduo_2 = Pessoa(Nome = Nome_Pessoa, Idade = Idade_Pessoa, Peso = Peso_Pessoa, Gênero = Gênero_Pessoa)

print (f'Seu Nome é {Indivíduo.Nome} com Idade de {Indivíduo.Idade} Anos, Peso de {Indivíduo.Peso} e Gênero {Indivíduo.Gênero}')

# -> Questão 3:

class Funcionário:
    def __init__(self, Id:int, Nome:str, Cargo:str, Salário:float) -> None:
        self.Id = Id
        self.Nome = Nome
        self.Cargo = Cargo
        self.Salário = Salário

class Empresa:
    def __init__(self) -> None:
        self.Lista_Funcionários = []
        self.Id = 0
    def Adicionar (self):
        Nome = str(input('Nome do Funcionário(a): '))
        Cargo = str(input('Cargo do Funcionário(a): '))
        Salário = float(input('Salário do Funcionário(a): '))
        
        Funcionário = Funcionário (Id = self.Id, Nome = Nome, Cargo = Cargo, Salário = Salário)
        self.Lista_Funcionários.append(Funcionário)

        self.Id += 1
    
    def Remover (self):
        for Funcionário in self.Lista_Funcionários:
            print (f'{Funcionário.Id} - {Funcionário.Nome} | {Funcionário.Cargo}')
        
        Funcionário_A_Remover = str(input('Digite o Id do Funcionário a Remover: '))
        
        if Funcionário_A_Remover >= 0 and Funcionário_A_Remover < len(self.Lista_Funcionários):
            for Funcionário_A_Remover in self. Lista_Funcionários:
                if Funcionário.Id == Funcionário_A_Remover:
                    self.Lista_Funcionários.remove(Funcionário)

    def Listar (self):
        for Funcionário in self.Lista_Funcionários:
            print (f'''
            Id: {Funcionário.Id} 
            Nome: {Funcionário.Nome}
            Cargo: {Funcionário.Cargo}
            Salário: {Funcionário.Salário}
''')

Empresa_1 = Empresa()

while True:
    Menu = int(input('''
1 - Adicionar
2 - Remover
3 - Listar
0 - Sair
'''))
    match Menu:
        case 1:
            print(Empresa_1.Adicionar())
        case 2:
            print(Empresa_1.Remover())
        case 3:
            print(Empresa_1.Listar())
        case 0:
            break
        case _:
            print ("Opção Inválida")