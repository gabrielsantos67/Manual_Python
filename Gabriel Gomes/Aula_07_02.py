# Utilizando o while para repetição com o 999 para sair
n = int(input("Digite um número para ser somado: [999 - para parar]"))
soma = 0
while n!= 999:
    soma += n
    n = int(input("Digite outro número para ser somado com os anteriores: [999 - para sair]"))
print("soma = {}".format(soma))

# Utilizando if e else
senha = "54321"
leitura = " "
while (leitura != senha):
    leitura = input("Digite a senha: ")
    if leitura == senha:
        print("Acesso Liberado")
    else:
        print("Acesso Negado")

# Pede ao usuário o número de termos de Fibonacci que ele deseja gerar e o armazena como um número inteiro
qtde = int(input("Quantos termos de fibonacci você deseja? "))
# Inicializa o primeiro termo de Fibonacci como 0
anterior = 0 
# Inicializa o segundo termo de Fibonacci como 1
atual = 1
# Inicializa um contador para rastrear quantos termos já foram gerados
contador = 1 
# Enquanto o contador for menor ou igual ao número de termos desejados
while contador <= qtde:
    # Imprime o termo atual da sequência de Fibonacci
    print("{} -".format(atual),end=" ")
    # Calcula o próximo termo da sequência de Fibonacci somando os dois últimos termos
    proximo = anterior + atual
    # Atualiza o valor anterior para o atual
    anterior = atual
    # Atualiza o valor atual para o próximo
    atual = proximo
    # Incrementa o contador para acompanhar o progresso
    contador += 1
    # Imprime o número do termo atual
    print(f"{contador}")
# Após o loop, quando todos os termos desejados foram gerados e impressos
print("Fim do programa de Fibonacci")


# Inicializa a variável de soma como 0
soma = 0
# Inicializa a quantidade de números digitados como 1
qtdenumeros = 1
# Inicializa a resposta como "s" para iniciar o loop
resp = "s"
# Inicia um loop enquanto a resposta for "s" (sim)
while resp == "s":
    # Solicita que o usuário digite um número e o armazena em 'n'
    n = int(input("Digite um número: "))
    # Se for o primeiro número digitado, define-o como o maior e o menor número até agora
    if qtdenumeros == 1:
        maior = n
        menor = n 
    # Se o número digitado for maior que o maior número até agora, atualiza o maior número
    if n > maior:
        maior = n
    # Se o número digitado for menor que o menor número até agora, atualiza o menor número
    if n < menor:
        menor = n
    # Adiciona o número à soma total
    soma += n 
    # Pergunta ao usuário se deseja continuar digitando
    resp = input("Deseja continuar digitando? s/n ")
    # Valida se a resposta é válida, se não for, solicita uma resposta correta
    while resp != "s" and resp != "n":
        resp = input("Informe corretamente se deseja continuar digitando: s/n")
    # Se o usuário deseja continuar digitando, incrementa a quantidade de números
    if resp == "s":
        qtdenumeros += 1

# Após o loop, quando o usuário termina de digitar números
# Imprime a quantidade de números digitados
print("Quantidade de números somados:{}".format(qtdenumeros))
# Imprime a soma total dos números digitados
print(f"soma = {soma}")
# Imprime o menor número digitado
print(f"menor número entre os digitados foi {menor}")
# Imprime o maior número digitado
print(f"maior número entre os digitados foi {maior}")

# Utiliza para contar os numeros somados e somar
soma = cont = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    cont += 1 
    soma += n 
print(f"Você somou {cont} números")
print(f"A soma de todos foi {soma}")

#Par ou impar usando o while
import random
ptsusuario = ptscomputador = 0
while True:
    n = int(input("Qual número entre 0 a 10? "))
    parouimpar = input("Responda p/i\nPar ou ímpar?")
    while parouimpar != "p" and parouimpar  != "i":
        parouimpar = input("responda: p/n\nResposta inválida? ")
    computador = random.randint(0,10)
    soma = n + computador
    if soma %2 == 0 and parouimpar == "p":
        ptsusuario +=1
    elif soma %2 == 1 and parouimpar == "i":
        ptsusuario +=1
    else:
        ptscomputador += ptscomputador
        break
print(f"Você venceu {ptsusuario} partidas")
print(f"Você venceu {ptscomputador} partidas")

# Utilizando o for faça uma tabuada
# Solicita ao usuário que digite um número e armazena-o como um número inteiro
numero = int(input("Digite um número: "))
# Imprime o cabeçalho da tabuada para o número digitado pelo usuário
print(f"Tabuada do {numero}")
# Itera sobre os números de 1 a 10 usando um loop for
for i in range(1, 11):
    # Calcula o resultado da multiplicação entre o número digitado e o número atual do loop
    result = numero * i
    # Imprime a operação de multiplicação e seu resultado formatados
    print(f"{numero} X {i} = {result}")

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