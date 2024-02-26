# -> Exercício 1:

class Calculadora:
    def __int__(self) -> None:
        self.Resultado = 0
    
    def Soma (self, Number_1:float, Number_2:float):
        self.Resultado = Number_1 + Number_2
        return self.Resultado

    def Subtração (self, Number_1:float, Number_2:float):
        self.Resultado = Number_1 - Number_2
        return self.Resultado

    def Multiplicação (self, Number_1:float, Number_2:float):
        self.Resultado = Number_1 * Number_2
        return self.Resultado

    def Divisão (self, Number_1:float, Number_2:float):
        if Number_2 != 0:
            self.Resultado = Number_1 / Number_2
            return self.Resultado
        else:
            self.Resultado = "Condição de Cálculo Inconsistente" 

Calculadora_1 = Calculadora() # Muito Importante Instanciar Antes de Codar

while True:

    Number_1 = float(input("Digite o 1º Número: ")) # Tratamento de Erro por Type Diferente é Matéria Avançada
    Number_2 = float(input("Digite o 2º Número: "))

    Menu = int(input("""
    Escolha uma operação
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    0 - Sair
"""))
    match Menu:
        case 1:
            print (Calculadora_1.Soma (Number_1 = Number_1, Number_2 = Number_2))
        case 2:
            print (Calculadora_1.Subtração (Number_1 = Number_1, Number_2 = Number_2))
        case 3:
            print (Calculadora_1.Multiplicação (Number_1 = Number_1, Number_2 = Number_2))
        case 4:
            print (Calculadora_1.Divisão (Number_1 = Number_1, Number_2 = Number_2))
        case 0:
            break
        case _:
            print ("Opção Inválida")

# -> Exercício 2:
            
class Gatelho:
    def __init__(self, Name:str, Years:int, Weight:float, Color:str, Race:str) -> None:
        self.Name = Name
        self.Years = Years
        self.Weight = Weight
        self.Color = Color
        self.Race = Race
    
    def Miar (self) -> str:
        return f'O Gatelho {self.Name} Está Miando'
    
    def Comer (self) -> str:
        return f'O Gatelho {self.Name} Está Comendo'

    def Info (self):
        return f'O Gatelho {self.Name}, tem {self.Years} Anos, Pesa {self.Weight} Kg de Cor {self.Color} e Raça {self.Race}'
    
Name_1 = str(input('Nome: '))
Years_1 = int(input('Years: '))
Weight_1 = float(input('Weight: '))
Color_1 = str(input('Color: '))
Race_1 = str(input('Race: '))
    
Gatelho_1 = Gatelho (Name = Name_1, Years = Years_1, Weight = Weight_1, Color = Color_1, Race = Race_1)
Gatelho_2 = Gatelho (Name = 'Salem', Years = 100, Weight = 2, Color = 'Preto', Race = 'Pedgree')

print (Gatelho_1.Miar())
print (Gatelho_1.Comer())
print (Gatelho_1.Info())

print (Gatelho_2.Miar())
print (Gatelho_2.Comer())
print (Gatelho_2.Info())