# -> Exercício 1:

class Animal:
    def __init__(self, Raça:str, Cor:str, Peso:float) -> None:
        self.Raça = Raça
        self.Cor = Cor
        self.Peso = Peso
    
    def Emitir_Som (self):
        return 'Som Indefinido'
    
class Cachorro (Animal):
    def __init__(self, Nome:str, Raça:str, Cor:str, Peso:float) -> None:
        super().__init__(Nome, Raça, Cor, Peso)

    def Pegar_Bolinha (self):
        return 'O Cachorro Pegou a Bolinha'
    
    def Emitir_Som (self):
        return 'Au Au'  # Polimorfismo é a Mudança do Método da Class Principal pela Sub-Class
    
class Gato (Animal):
    def __init__(self, Nome:str, Raça:str, Cor:str, Peso:float, Cor_Olho:str) -> None:
        super().__init__(Nome, Raça, Cor, Peso)
        self.Cor_Olho = Cor_Olho

    def Amassar_Pãozinho(self):
        return f"O Gato {self.Nome} Está Amassando Pãozinho"
    
    def Emitir_Som (self):
        return 'Miau'  # Polimorfismo é a Mudança do Método da Class Principal pela Sub-Class   

Cachorro_1 = Cachorro (Raça = "Pitbull", Cor = "Bege", Peso = 8.3)
Gato_1 = Gato (Raça = "Angorá", Cor = "Branco", Peso = 3.5, Cor_Olho = "Azul")

print(Cachorro_1.Emitir_Som())
print(Gato_1.Emitir_Som())

# -> Exercício 2:

class Veículo:
    def __init__(self, Marca:str, Modelo:str, Cor:str, Ano:int) -> None:
        self.__Marca = Marca
        self.__Modelo = Modelo
        self.__Cor = Cor
        self.__Ano = Ano
        self.__Velocidade_Atual = 0

    def Get_Marca (self):
        return self.__Marca

    def Set_Marca (self, Nova_Marca):
        self.__Marca = Nova_Marca
        return 'Marca Alterada com Sucesso'

    def Get_Modelo (self):
        return self.__Modelo

    def Set_Modelo (self, Novo_Modelo):
        self.__Modelo = Novo_Modelo
        return 'Modelo Alterado com Sucesso'

    def Get_Cor (self):
        return self.__Cor

    def Set_Cor (self, Nova_Cor):
        self.__Cor = Nova_Cor
        return 'Cor Alterada com Sucesso'

    def Get_Ano (self):
        return self.__Ano

    def Set_Ano (self, Novo_Ano):
        self.__Ano = Novo_Ano
        return 'Ano Alterado com Sucesso'
    
    def Acelerar (self, Velocidade_Acelerada:float):
        self.__Velocidade_Atual += Velocidade_Acelerada
        return f'O Veículo {self.__Marca} {self.__Modelo} Está Acelerado'

    def Frear (self):
        if self.__Velocidade_Atual >= 10:
            self.__Velocidade_Atual -= 10
            return f'O Veículo {self.__Marca} {self.__Modelo} Está Freando'
        else:
            self.__Velocidade_Atual = 0
            return f'O Veículo Parou'
    
    def Buzinar (self):
        return 'Som Indefinido'

class Carro (Veículo):
    def __init__(self, Marca: str, Modelo: str, Cor: str, Ano: int, Velocidade_Atual: int, Portas:int):
        super().__init__(Marca, Modelo, Cor, Ano, Velocidade_Atual)
        self.__Portas = Portas

    def Get_Portas (self):
        return self.__Portas

    def Set_Portas (self, Novas_Portas):
        self.__Portas = Novas_Portas
        return 'Portas Alteradas com Sucesso' 
    
    def Buzinar (self):
        return 'Bi Bi!'
    
class Navio (Veículo):
    def __init__(self, Marca: str, Modelo: str, Cor: str, Ano: int, Velocidade_Atual: int):
        super().__init__(Marca, Modelo, Cor, Ano, Velocidade_Atual)

    def Buzinar (self):
        return 'Foooooooom!'
    
Carro_1 = Carro (Marca = 'Dodge', Modelo = 'Challenger', Cor = 'Azul', Ano = 1985, Velocidade_Atual = 100, Portas = 2)
Navio_1 = Navio (Marca = 'Cruseiro', Modelo = 'Inter_Oceânico', Cor = 'Branco', Ano = 2023, Velocidade_Atual = 200)

Nova_Cor_Carro_1 = str(input("Nova Cor do Carro: "))
Carro_1.Set_Cor(Nova_Cor = Nova_Cor_Carro_1)
print (Carro_1.Set_Cor(Nova_Cor_Carro_1))
print (Carro_1.Get_Cor())

Novas_Portas_Carro_1 = int(input('Nova Quantidade de Portas: '))
Carro_1.Set_Portas(Novas_Portas = Novas_Portas_Carro_1)
print (Carro_1.Set_Portas(Novas_Portas_Carro_1))

print (Carro_1.Acelerar(300))
print (Carro_1.Frear())
print (Carro_1.Buzinar())
