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