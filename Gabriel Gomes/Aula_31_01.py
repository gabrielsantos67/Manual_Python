# 1) Crie um programa que exiba a seguinte frase
#"Meu nome é {nome} tenho {idade} anos e moro na cidade de {cidade}."
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
cidade = str(input("Digite sua cidade: "))

# Usando o F para formatação abreviação do format
print(f"Meu nome é {nome} tenho {idade} anos e moro na cidade de {cidade}.")

# 2) Crie um programa que devolva uma conta com cada operador lógico: +,-,*,/,%,**,//
N1 = int(input("Digite um número: "))
N2 = int(input("Digite um número: "))

print("O resultado da sua soma é: ", N1+N2)
print("O resultado da sua subtração é: ", N1-N2)
print("O resultado da sua multiplicação é: ", N1*N2)
result = N1/N2
print(f"O resultado da sua divisão é: {result:.2f}")
print("O resto da sua divisão é: ", N1%N2)
print("O resultado da sua exponenciação é: ", N1**N2)
print("O resultado da sua divisão inteira é: ", N1//N2)

# 2) Crie um programa que devolva uma conta com cada operador de comparação: ==, !=, <, >, >=, <=

N1 = int(input("Digite um número: "))
N2 = int(input("Digite um número: "))

print(N1 == N2)
print(N1 != N2)
print(N1 < N2)
print(N1 > N2)
print(N1 >= N2)
print(N1 <= N2)

# 3) Faça um programa que devolva o salário mais o acréscimo de 15%
Salario = 1000

salario_final = Salario * 0.45

sala_acre = salario_final + Salario 

print(f"O seu salário atual é: R${Salario:.2f} Após o acréscimo seu salário será de: R${sala_acre:.2f}")

# 4) elabore um programa que exba o lucro da empresa

faturamento = int(input("Digite o Faturamento mensal da sua empresa: "))
custo = int(input("Digite o custo mensal da sua empresa: "))

lucro = faturamento - custo

print(f"O lucro mensal da sua empresa é: R${lucro:.2f}")

# 5) Faça um programa que devolva "olá!!" + o seu nome
nome= str(input("Digite o seu nome: "))
print("Olá!!",nome)

# 6) calcule a base de um triângulo
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

area=(base*altura)/2

print(f"A área do seu triângulo é: {area:.2f}")