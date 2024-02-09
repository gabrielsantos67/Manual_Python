# Define uma função chamada "hello"
def hello():
    # Imprime a mensagem "Olá Mundo!!" quando a função é chamada
    print("Olá Mundo!!")
# Chama a função "hello", que imprime a mensagem "Olá Mundo!!"
hello()



# Define uma função chamada "maior" que aceita dois parâmetros, x e y
def maior(x, y):
    # Verifica se x é maior que y
    if x > y:
        # Se x for maior que y, imprime o valor de x
        print(x)
    else:
        # Se y for maior ou igual a x, imprime o valor de y
        print(y)
# Chama a função "maior" com os argumentos 4 e 7
maior(4, 7)



# Define uma função chamada "soma" que aceita dois parâmetros, x e y
def soma(x, y):
    # Calcula a soma dos dois parâmetros e armazena o resultado na variável "total"
    total = x + y
    # Imprime o resultado da soma
    print("Total soma = ", total)
# Programa principal
# Define uma variável chamada "total" com o valor 10
total = 10
# Chama a função "soma" com os argumentos 3 e 5
soma(3, 5)
# Imprime o valor da variável "total" do programa principal
print("Total principal = ", total)



# Define uma função chamada "soma" que aceita dois parâmetros, x e y
def soma(x, y):
    # Calcula a soma dos dois parâmetros e armazena o resultado na variável "total"
    total = x + y
    # Retorna o valor da variável "total"
    return total
# Programa principal
# Chama a função "soma" com os argumentos 3 e 5 e armazena o resultado na variável "s"
s = soma(3, 5)
# Imprime o valor retornado pela função "soma"
print("soma = ", s)

