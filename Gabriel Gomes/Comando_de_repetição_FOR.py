# Comando usado para repetição 
for numero in range(2):
    print(numero)

# O primeiro número é o start, o segundo o stop e 
# o terceiro a ordem de contagem EX:(2 em 2)
for numero in range(1,3,2):
    print(numero)

# Comando for usando strings
palavra = 'Google'
for palavra in 'Google':
    print(palavra)

# Comando de repetição com inserção de dados string
nome = str(input("Digite o seu nome: "))
for nome in nome:
    print(nome)

# Comando para exibir o nome com uma frase e no final 
# retornar o nome colocado no input
nome = str(input("Digite o seu nome: "))
teste = nome
for nome in nome:
    print(f"{nome} está dentro da palavra {teste}")

# simulando uma compra
compra_confirmada = True
dados_compra = 'compra no valor de R$12.50 e entrega confirmada'
if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu email')
else:
    print('falha na compra')

# simulando uma compra usando "for"
compra_confirmada = True
dados_compra = 'compra no valor de R$12.50 e entrega confirmada'
for enviar in range(3):
      if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu email')
else:
    print('falha na compra')

# O mesmo utilizando o break para ele para o for, assim executando apenas uma vez
compra_confirmada = True
dados_compra = 'compra no valor de R$12.50 e entrega confirmada'
for enviar in range(3):
      if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu email')
        break
else:
    print('falha na compra')

# criação do outer for loop, outer mean first number
for numero in range(1,6):
    print('Produto', str(numero))

    # criação do inner for loop, inner mean second number
    for num2 in range(7):
        print(numero, num2)

# 'end' é utilizado para imprimir na mesma linha
palavra = 'FANTASTICO'

for spaco in palavra:
    print(spaco, end = '') # então (end = '') é usado para impedir que pule linha

# utilizado a inserção de dados
palavra = str(input("Digite a palavra: "))
for spaco in palavra:
    print(spaco, end = ' ')

# Utilizamos esse comando para fazer um retangulo com simbolos
linhas = 6
colunas = 6
simbol = "@"
for l in range(linhas):
    for c in range(colunas):
        print(simbol, end = ' ')
    print()
