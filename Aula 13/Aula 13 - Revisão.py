# -> Exercício 1:

class Dispositivo:
    def __init__(self, Marca:str, Modelo:str, Cor:str, Ligado:bool) -> None:
        self.Marca = Marca
        self.Modelo = Modelo
        self.Cor = Cor
        self.Ligado = False
    
    def Ligar (self):
        if self.Ligado == False:
            self.Ligado = True
            return f'O Celular {self.Modelo} Ligou'
        else:
            return 'O Celular Já Está Ligado'
    
    def Desligar (self):
        if self.Ligado:
            self.Ligado = False
            return f'O Celular {self.Modelo} Desligou'
        else:
            return 'O Celular Já Está Desligado'
    
class Smartphone (Dispositivo):
    def __init__(self, Marca: str, Modelo: str, Cor: str, Ligado: bool, Sistema_Operacional:str) -> None:
        super().__init__(Marca, Modelo, Cor, Ligado)
        self.Sistema_Operacional = Sistema_Operacional
    
    def Chamada (self, Número:str):
        if self.Ligado:
            return f'O {self.Marca} {self.Modelo} Está Chamando o Número {Número}'
        else:
            return f'O Smartphone Está Desligado, Impossível Realizar Chamada'
    
class Notebook (Dispositivo):
    def __init__(self, Marca: str, Modelo: str, Cor: str, Ligado: bool, SSD:bool) -> None:
        super().__init__(Marca, Modelo, Cor, Ligado)
        self.SSD = SSD

    def Acessar_Site (self, Site:str):
        if self.Ligado and self.SSD:
            return f'O Notebook Acessa o Site {Site} Rapidamente'
        elif self.Ligado and self.SSD == False:
            return f'O Notebook Acessa o Site {Site} Lentamente'
        else:
            return f'O Notebook Está Impossibilitado de Acessar o Site {Site}, Ligue o Dispositivo'
        
Número = str(input('Digite o Número a ser Chamado: '))
Site = str(input('Digite o Site a ser Acessado: '))
Smartphone_1 = Smartphone (Marca = 'Iphone', Modelo = '14', Cor = 'Preto', Ligado = True, Sistema_Operacional = 'IOS')
Smartphone_2 = Smartphone (Marca = 'Samsung', Modelo = 'A50', Cor = 'Preto', Ligado = False, Sistema_Operacional = 'Android')
Notebook_1 = Notebook (Marca = 'DELL', Modelo = 'G15', Cor = 'Preto', Ligado = True, Sistema_Operacional = 'Windowns 12')
Tablet_1 = Dispositivo (Marca = 'Motorolla', Modelo = 'Super', Cor = 'Cinza', Ligado = True)

print (Smartphone_1.Ligar())
print (Smartphone_1.Chamada('85999912345'))
print (Smartphone_1.Desligar())
print (Smartphone_1.Chamada('85999912345'))

print (Smartphone_2.Ligar())
print (Smartphone_2.Chamada('85999912345'))
print (Smartphone_2.Desligar())
print (Smartphone_2.Chamada('85999912345'))

print (Notebook_1.Ligar())
print (Notebook_1.Acessar_Site('www.google.com'))
print (Notebook_1.Desligar())
print (Notebook_1.Acessar_Site('www.google.com'))

print (Tablet_1.Ligar())
print (Tablet_1.Desligar())