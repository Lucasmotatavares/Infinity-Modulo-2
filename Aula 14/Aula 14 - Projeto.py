# -> Projeto:

class Livro:
    def __init__(self, Título:str, Autor:str, Id:int) -> None:
        self.Título = Título
        self.Autor = Autor
        self.Id = Id
        self.Disponível = True

class Membro:
    def __init__(self, Nome:str, Id:int) -> None:
        self.Nome = Nome
        self.Id = Id
        self.Histórico_Livros = []

class Biblioteca:
    def __init__(self) -> None:
        self.Catálogo_Livros = []
        self.Lista_Membros = []
        self.Id_Livro = 1
        self.Id_Membro = 1
    
    def Add_Livro (self):
        while True:
            try:
                Título_Livro = str(input("Digite o Título do Livro: ")).strip()
                Autor_Livro = str(input("Digite o Autor do Livro: ")).strip()
            except:
                print ('Error, Tente Novamente')
            Instância_Livro = Livro(Título=Título_Livro, Autor=Autor_Livro, Id=self.Id_Livro) # Dúvida Sobre Utilizar Dicionário Aqui
            self.Catálogo_Livros.append(Instância_Livro)
            self.Id_Livro += 1
            print (f'O Livro {Autor_Livro}, {Título_Livro} foi Adicionado ao Catálogo!')

    def Add_Membro (self):
        while True:
            try:
                Nome_Membro = str(input("Digite o Nome do Membro: ")).strip()
            except:
                print ('Error, Tente Novamente')
            Instância_Membro = Membro(Nome=Nome_Membro,Id=self.Id_Membro)
            self.Lista_Membros.append(Instância_Membro)
            self.Id_Membro += 1
            print (f'O Membro {Nome_Membro} foi Adicionado!')

    def Emprestar_Livro (self): # Verificar Necessidade de Existência do Id Digitado
        while True:
            try:
                Id_Membro_Escolhido = int(input("Digite Id do Membro Alugará o Livro: "))
                break
            except:
                print ('Digite um Número, Tente Novamente')
        for Member in self.Lista_Membros:
            if Member.Id == Id_Membro_Escolhido:
                while True:
                    try:
                        Id_Livro_Escolhido = int(input("Digite Id do Livro: "))
                        break
                    except:
                        print ('Digite um Número, Tente Novamente')
                for Book in self.Catálogo_Livros:
                    if Book.Id == Id_Livro_Escolhido and Book.Disponível == True:
                        Book.Disponível = False
                        Member.Histórico_Livros.append(Book)
                        print (f'O {Book.Título} de {Book.Autor} foi Alugado por {Member.Nome}')

    def Devolver_Livro (self):
        while True:
            try:
                Id_Livro_Escolhido = int(input("Digite Id do Livro: "))
                break
            except:
                print ('Digite um Número, Tente Novamente')
        for Book in self.Catálogo_Livros:
            if Book.Id == Id_Livro_Escolhido and Book.Disponível == False:
                Book.Disponível = True
                print (f'O {Book.Título} de {Book.Autor} foi Devolvido')

    def Pesquisar_Membro (self):
        try:
            Termo_Digitado = str(input('Digite uma das Opções [Nome, Id]: ')).strip()
            Membro_Não_Encontrado = True
            for Member in self.Lista_Membros:
                if Member.Nome == Termo_Digitado or str(Member.Id) == Termo_Digitado:
                    Membro_Não_Encontrado = False
                    print (f'''
                        Info do Membro:
                        Nome: {Member.Nome}
                        Id: {Member.Id} 
                        Histórico: {Member.Histórico_Livros}
''')
            if Membro_Não_Encontrado: # Considera-se True
                print ('Membro Não Consta no Banco de Dados')
        except:
            print ('Informação Inválida, Utilize o Menu e Tente Novamente')

    def Pesquisar_Livro (self):
        try:
            Termo_Digitado = str(input('Digite uma das Opções [Título, Autor, Id]: ')).strip()
            Livro_Não_Encontrado = True
            for Book in self.Catálogo_Livros:
                if Book.Título == Termo_Digitado or Book.Autor == Termo_Digitado or str(Book.Id) == Termo_Digitado:
                    Livro_Não_Encontrado = False
                    print (f'''
                        Info do Livro:
                        Título: {Book.Título}
                        Autor: {Book.Autor}
                        Id: {Book.Id} 
                        Status: {Book.Disponível}
''')
            if Livro_Não_Encontrado: # Considera-se True
                print ('Livro Não Consta no Banco de Dados')
        except:
            print ('Informação Inválida, Utilize o Menu e Tente Novamente')

Instância_Biblioteca = Biblioteca ()
    
while True:
    Menu = int(input("""O que Deseja Fazer? [1/2/3/4/5/6/0]
                    1 - Adicionar Livro
                    2 - Emprestar Livro
                    3 - Devolver Livro
                    4 - Pesquisar Livro
                    5 - Adicionar Membro
                    6 - Pesquisar Membro
                    0 - Sair do Programa
                    """))
    
    match Menu:
        case 0:
            print("Programa Encerrado!")
            pass
        case 1:
            Instância_Biblioteca.Add_Livro () # Preencher Parênteses Apenas se Vier um Input antes de Chamar o Método 
            pass
        case 2:
            Instância_Biblioteca.Emprestar_Livro ()
            pass       
        case 3:
            Instância_Biblioteca.Devolver_Livro ()
            pass       
        case 4:
            Instância_Biblioteca.Pesquisar_Livro ()
            pass
        case 5:
            Instância_Biblioteca.Add_Membro ()
            pass
        case 6:
            Instância_Biblioteca.Pesquisar_Membro()
            pass
        case _:
            print ('Preencha Corretamente o Campo Menu')
            break