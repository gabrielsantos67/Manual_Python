#função type serve para mostrar o tipo da sua variavel no print
B = "olá"
print(B, type(B))

#atribuições ou programas reduzidos
x = 5
x+=5
print(x)

#estrutura condicional
N1 = int(input("Primeiro valor: "))
N2 = int(input("Segundo valor: "))

if N1 > N2:
    print(N1,"é maior que",N2)
else:
    print(N2, "é maior que",N1)

# criar um código que exiba a idade do carro, <= 3 carro novo, >= 3 seu carro é velho
AF = int(input("Digite o ano de fabricação do seu carro: "))
result = 2024 - AF 

if result <= 3:
    print(f"Seu carro foi fabricado no ano de {AF}, portanto ele é um carro novo")
if result > 3:
    print(f"Seu carro foi fabricado no ano de {AF}, portanto ele é um carro antigo")

# Condicional usando o else
a = int(input("Digite um Número: "))
if a > 7:
    print("Está no if")
else:
    print("Está no else")

# Condicional com constante 
a = 3
if a > 7:
    print("Está no if")
else:
    print("Está no else")

# Calcular o valor do plano telefonico
# abaixo de 200 cobrar R$ 0,20/m, acima de 400 cobrar R$0,15
# entre 200 e 400 cobrar R$0,18.

min = int(input("Digite a quantidade de minutos usados no mês: "))
if min < 200:
    preco = 0.20
elif min > 400:
    preco = 0.15
else:
    preco = 0.18

calculo = min*preco
print(f"Este mês voce utilizou, e tera que pagar R${calculo:6.2f} pelo seu plano")

# Faça um programa que peça a entrada das notas e devolva a média junto ao status do aluno
# Digitação das notas
Nt1 = float(input("Digite a nota do aluno: ")) 
Nt2 = float(input("Digite a nota do aluno: ")) 
Nt3 = float(input("Digite a nota do aluno: ")) 
Nt4 = float(input("Digite a nota do aluno: ")) 

# Calculo da média
media = (Nt1+Nt2+Nt3+Nt4)/4

# Laço de repetição para definir o aprovado, reprovado e recuperação 
if media >= 6:
    print(f"Sua média final foi: {media:.2f}, Você está aprovado!! :)")

elif media < 3:
    print(f"Sua média final foi: {media:.2f}, Você está reprovado! :(") 

else:
    print(f"Sua média final foi: {media:.2f}, Você está de recuperação! :/")





    


