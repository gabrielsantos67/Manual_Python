#É uma estrutura que vai devolver na tela após passar pelas condições determinadas

#estrutura condicional 
N1 = int(input("Primeiro valor: "))
N2 = int(input("Segundo valor: "))

if N1 > N2:
    print(N1,"é maior que",N2)
else:
    print(N2, "é maior que",N1)

#Ex:
#criar um código que exiba a idade do carro, <= 3 carro novo, >= 3 seu carro é velho
AF = int(input("Digite o ano de fabricação do seu carro: "))
result = 2024 - AF 

if result <= 3:
    print(f"Seu carro foi fabricado no ano de {AF}, portanto ele é um carro novo")
if result > 3:
    print(f"Seu carro foi fabricado no ano de {AF}, portanto ele é um carro antigo")

#Calculo do imposto sobre o salário
salario = float(input("Digite o salário para o cálculo de imposto: "))
base = salario 
imposto = 0 
if base > 3000:
    imposto = imposto +((base - 3000)* 0.35)
    base = 3000
if base >= 1000:
    imposto = imposto + ((base + salario)* 0.20)
print("Salário: R$%6.2f, Imposto a pagar: R$%6.2f" % (salario, imposto))

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
