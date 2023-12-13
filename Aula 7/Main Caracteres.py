import Caracteres as Cr 
# Apelidou Biblioteca
# Precisa Escrever Biblioteca Antes da Função

Texto_Usuário = str(input('String Digitada: ')).lower().strip()

print (Cr.Qtd_Caracteres(String = Texto_Usuário))
print (Cr.Qtd_Consoantes(String = Texto_Usuário))
print (Cr.Qtd_Vazios(String = Texto_Usuário))
print (Cr.Qtd_Vogais(String = Texto_Usuário))

from Caracteres import * 
# Não Precisa Escrever Biblioteca Antes da Função

Texto_Usuário = str(input('String Digitada: ')).lower().strip()

print (Qtd_Caracteres(String = Texto_Usuário))
print (Qtd_Consoantes(String = Texto_Usuário))
print (Qtd_Vazios(String = Texto_Usuário))
print (Qtd_Vogais(String = Texto_Usuário))
