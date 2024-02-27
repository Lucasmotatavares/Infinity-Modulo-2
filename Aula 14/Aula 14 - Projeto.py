# -> Projeto:
while True:

    class Livro:
        def __init__(self, Título=str, Autor=str, Id=int) -> None:
            self.Título = Título
            self.Autor = Autor
            self.Id = Id
            self.Disponível = True

    class Membro:
        def __init__(self, Nome=str, Id=int) -> None:
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
            Título_Livro = str(input("Digite o Título do Livro: "))
            Autor_Livro = str(input("Digite o Autor do Livro: "))
            Instância_Livro = Livro(Título=Título_Livro, Autor=Autor_Livro, Id=self.Id_Livro) # Dúvida Sobre Utilizar Dicionário Aqui
            self.Catálogo_Livros.append(Instância_Livro)
            self.Id_Livro += 1
            print (f'O Livro {Autor_Livro}, {Título_Livro} foi Adicionado ao Catálogo!')

        def Add_Membro (self):
            Nome_Membro = str(input("Digite o Nome do Membro: "))
            Instância_Membro = Membro(Nome=Nome_Membro,Id=self.Id_Membro)
            self.Lista_Membros.append(Instância_Membro)
            self.Id_Membro += 1
            print (f'O Membro {Nome_Membro} foi Adicionado!')

        def Emprestar_Livro (self): # Verificar Necessidade de Existência do Id Digitado
            try:
                Id_Livro = int(input("Digite qual o Id do Livro: "))
                Id_Membro = int(input("Digite qual o Id do Membro: "))
            except:
                print("Informação Inválida Detectada, Tente Novamente")
                return
        
            for Book in self.Catálogo_Livros:
                if Id_Livro == Book.Id:
                    Book.Disponível = False
                    for Member in self.Lista_Membros:
                        if Id_Membro == Member.Id:
                            Member.Histórico_Livros.append(Book)
                            print (f'O Livro de Id {Book} foi Emprestado!')
                            return

        def Devolver_Livro (self):
            try:
                Id_Livro = int(input("Qual o Id do livro que você Deseja Devolver?: "))
            except:
                print("Id Inválido, Tente Novamente")
                return
        
            for Book in self.Catálogo_Livros:
                if Id_Livro == Book.Id:
                    Book.Disponível = True
                    print (f'O Livro de Id {Book} foi Devolvido!')

        def Pesquisar_Membro (self, Nome:str):
            # Member = str(input('Digite o Nome do Membro: '))
            for Member in self.Lista_Membros:
                if Member.Nome.lower() == Nome.lower():
                    print (f'O {Member.Nome} Possui o Id {Member.Id}')
                    return Member.Id
            if not self.Lista_Membros:
                print (f'Membro Não Consta no Banco de Dados')

        def Pesquisar_Livro (self, Título:str):
            # Book = str(input('Digite o Título do Livro: '))
            for Book in self.Catálogo_Livros:
                if Book.Título.lower() == Título.lower():
                    print (f'O {Book.Título} Possui o Id {Book.Id}')
                    return Book.Id
            if not self.Catálogo_Livros:
                print (f'Livro Não Consta no Banco de Dados')

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
        
        Instância_Biblioteca = Biblioteca ()
        
        match Menu:
            case 0:
                print("Programa Encerrado!")
                break
            case 1:
                Instância_Biblioteca.Add_Livro ()
                break
            case 2:
                Instância_Biblioteca.Emprestar_Livro ()
                break       
            case 3:
                Instância_Biblioteca.Devolver_Livro ()
                break       
            case 4:
                Book = str(input('Digite o Título do Livro: '))
                Instância_Biblioteca.Pesquisar_Livro (Título = Book)
                break
            case 5:
                Instância_Biblioteca.Add_Membro ()
                break
            case 6:
                Member = str(input('Digite o Nome do Membro: '))
                Instância_Biblioteca.Pesquisar_Membro (Nome = Member)
                break
            case _:
                print ('Preencha Corretamente o Campo Menu')
                break