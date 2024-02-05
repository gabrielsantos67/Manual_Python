#Para este desafio, quero que você crie um código que imprima a frase “Bom dia <seu nome>  
name = str(input("Type your name: "))
print(f"Good Morning {name}")

# Para este, desafio quero que você declare duas variáveis: uma chamada ‘nome’, 
# que deve guardar seu primeiro nome como string, e oura chamada ‘idade’, que deve guardar a sua idade como um número inteiro. 
# Depois disso, quero que você imprima na tela uma frase que diga ‘Oi meu [nome] é e tenho [idade] anos.
name = str(input("Type your name: "))
old = int(input("Type your years old: "))
print(f"Hi my name is {name}, and i'm {old} years old.")

#Neste desafio, peço que declare duas varáveis: num1 que deve guardar o 
#número inteiro 10 e num2 que deve guardar o número de ponto flutuante 3.5. 
#depois disso, quero que você realize e imprima na tela o resultado da divisão de num1 por num2 
num1 = 10
num2 = 3.5
divi = num1/num2 
print(f"O resultado da divisão é: {divi:.2f}")

#Neste desafio, quero que você crie um código que pergunte o nome e a idade do usuário, 
#usando a função input(). Despois disso o código deve imprimir uma mensagem de boas-vindas 
#aparecendo o nome a idade e o seu endereço.
name = str(input("Type your name: "))
old = int(input("Type your years old: "))
add = input("Type your address: ")
print(f"Wellcome {name}, you has {old} years old and your address is {add} ")

#Neste desafio, quero que você crie um script que solicite ao usuário dois números. 
#Em seguida, seu script deve imprimir a soma, a subtração, a multiplicação, 
#a divisão e a exponenciação (o primeiro número elevado ao segundo números) desses dois números.
n1 = int(input("Type some number: "))
n2 = int(input("Type some number: "))

addition = n1+n2
subtraction = n1-n2
multiplication = n1*n2
division= n1/n2
exponentiation = n1**n2
print(f"the result of your addition is: {addition}")
print(f"the result of your subtraction is: {subtraction}")
print(f"the result of your multiplication is: {multiplication}")
print(f"the result of your division is: {division:.3f}")
print(f"the result of your exponentiation is: {exponentiation}")

#Para este desafio, quero que você use a função range() em for loop 
#para imprimir os números de 1 a 10 na tela 
for numero in range(1,11):
    print(numero, end = ' ')

# Calculo da passagem do busão
km = int(input("Digite a distância em quilometros de sua viagem: "))

if km > 200:
    preco = km * 0.45
else:
    preco = km * 0.50
print(f"O preço da sua passagem é: {preco}")