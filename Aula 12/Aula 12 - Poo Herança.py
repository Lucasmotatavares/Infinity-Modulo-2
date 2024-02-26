# -> Exercício 1:

class Veículo:
    def __init__(self, Marca:str, Modelo:str, Ano:int, Cor:str) -> None:
        self.Marca = Marca
        self.Modelo = Modelo
        self.Ano = Ano
        self.Cor = Cor

    def Ligar (self):
        return f'O Veículo {self.Modelo} Está Ligado'
    
    def Desligar (self):
        return f'O Veículo {self.Modelo} Está Desligado'

class Carro (Veículo):
    def __init__(self, Marca:str, Modelo:str, Ano:int, Cor:str, Portas:int) -> None:
        super().__init__(Marca, Modelo, Ano, Cor)
        self.Portas = Portas

    def Ar (self):
        return f'O Carro {self.Modelo} Ligou o Ar Condicionado'

class Moto (Veículo):
    def __init__(self, Marca:str, Modelo:str, Ano:int, Cor:str, Cilindradas:int) -> None:
        super().__init__(Marca, Modelo, Ano, Cor)
        self.Cilindradas = Cilindradas

    def Descanso (self):
        return f'A Moto {self.Modelo} Está Apoiada no Descanso'

Carro_1 = Carro(Marca = 'Fiat', Modelo = 'Uno', Ano = 2002, Cor = 'Prata', Portas = 2)
Moto_1 = Moto(Marca = 'BMW', Modelo = 'g310', Ano = 2023, Cor = 'Branco', Cilindradas = 300)


    
    