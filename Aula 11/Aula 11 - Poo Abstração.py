# -> Exercício 1:

class Celular:
    def __init__(self, Marca:str, Modelo:str, Cor:str, Ano:int, Armazenamento:int) -> None: # Pode Remover "-> None", Significa que a Função Retornará Nada
        # É de Bom Costume Codar os Mesmos Nomes no "Self" e nas Variáveis
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
Auto_Glass = bool(input(' Car_Auto_Glass = '))
# Dodge, Challenger, Orange, 1970, 2, False, False

Car_1 = Car(Brand = 'Wolkswagen', Model = 'Gol GTI 2.0', Color = 'Preto', Year = 1989, Doors = 2, Air_System = True, Auto_Glass = True)
Car_2 = Car(Brand = 'Ford', Model = 'Maverick Supercharger', Color = 'Azul', Year = 1979, Doors = 2, Air_System = False, Auto_Glass = False)
Car_3 = Car(Brand = Brand, Model = Model, Color = Color, Year = Year, Doors = Doors, Air_System = Air_System, Auto_Glass = Auto_Glass)

if Car_2.Auto_Glass:
    Car_2.Auto_Glass = 'Auto Glass: Check'
else:
    Car_2.Auto_Glass = 'Auto Glass: Uncheck'

if Car_3.Auto_Glass:
    Car_3.Auto_Glass = 'Auto Glass: Check'
else:
    Car_3.Auto_Glass = 'Auto Glass: Uncheck'

if Car_3.Air_System:
    Car_3.Air_System = 'Air System: Check'
else:
    Car_3.Air_System = 'Air System: Uncheck'


print (Car_1.Brand, Car_1.Model)
print (Car_2.Model, Car_2.Year, Car_2.Auto_Glass)
print (f'Car Brand {Car_3.Brand} Model {Car_3.Model} Color {Car_3.Color} Year {Car_3.Year}, {Car_3.Doors} Doors, Air System: {Car_3.Air_System}, Auto Glass: {Car_3.Auto_Glass}')


