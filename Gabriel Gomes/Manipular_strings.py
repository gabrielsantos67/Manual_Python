# Define uma variável chamada 'palavra' com o valor "Apostila de Python"
palavra = "Apostila de Python"

# len(): Retorna o comprimento da string 'palavra'
print(len(palavra))
# capitalize(): Retorna uma cópia da string 'palavra' com a primeira letra maiúscula e as demais minúsculas
print(palavra.capitalize())
# count(): Retorna o número de ocorrências da substring "o" na string 'palavra'
print(palavra.count("o"))
# startswith(): Retorna True se a string 'palavra' começa com a substring "Ap", caso contrário, retorna False
print(palavra.startswith("Ap"))
# endswith(): Retorna True se a string 'palavra' termina com a substring "Py", caso contrário, retorna False
print(palavra.endswith("Py"))
# isalnum(): Retorna True se todos os caracteres na string 'palavra' são alfanuméricos (letras ou números), caso contrário, retorna False
print(palavra.isalnum())

# Define uma variável de string chamada "palavra"
palavra = "Apostila de Python"
# Converte a string para minúsculas e imprime o resultado
print(palavra.lower())
# Converte a string para maiúsculas e imprime o resultado
print(palavra.upper())
# Inverte as maiúsculas e minúsculas dos caracteres na string e imprime o resultado
print(palavra.swapcase())
# Converte a string para o formato de título e imprime o resultado
print(palavra.title())
# Divide a string em uma lista de substrings com base nos espaços em branco e imprime a lista
print(palavra.split())



# Fatiar palavras
s = str(input("Digite uma palavra: "))
print(s[1:4])
print(s[2:])
print(s[:4])