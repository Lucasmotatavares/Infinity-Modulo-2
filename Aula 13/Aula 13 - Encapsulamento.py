# -> Exercício 1:

class Animal:
    def __init__(self, Nome:str, Raça:str, Cor:str, Peso:float) -> None:
        self.__Nome = Nome
        self.__Raça = Raça
        self.__Cor = Cor
        self.__Peso = Peso

    def Get_Raça (self):
        return self.__Raça

    def Set_Raça (self, Nova_Raça):
        self.__Raça = Nova_Raça
        return 'Raça Alterada com Sucesso'
    
    def Get_Cor (self):
        return self.__Cor

    def Set_Cor (self, Nova_Cor):
        self.__Cor = Nova_Cor
        return 'Cor Alterada com Sucesso'
    
    def Get_Peso (self):
        return self.__Peso

    def Set_Peso (self, Nova_Peso):
        self.__Peso = Nova_Peso
        return 'Peso Alterado com Sucesso'

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
    
Cachorro_1 = Cachorro (Nome = 'Chubchub', Raça = "Pitbull", Cor = "Bege", Peso = 8.3)
Gato_1 = Gato (Nome = 'Chachacha', Raça = "Angorá", Cor = "Branco", Peso = 3.5, Cor_Olho = "Azul")

print (Cachorro_1.Emitir_Som())
print (Gato_1.Emitir_Som())
