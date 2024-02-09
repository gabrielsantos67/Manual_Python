# Caracterizado pelo uso de [] 
# é possivel ter uma lista dentro da outra
# Define uma lista com diferentes tipos de elementos
L = [3, 'abacate', 9.7 , [5, 6, 3], "python", (3, "j")]
# Imprime o elemento na posição 2 da lista (índice 2)
print(L[2])
# Imprime o elemento na posição 3 da lista (índice 3), que é uma lista
print(L[3])
# Imprime o segundo elemento da lista que está na posição 3 da lista inicial
print(L[3][1])
# Define uma lista com diferentes elementos
L = [3, 'abacate', 9.7 , [5, 6, 3], "python", (3, "j")]
# Reatribui o elemento na posição 5 da lista para a entrada do usuário convertida em string
L[5] = str(input("Digite um número ou palavra: "))
# Imprime a lista atualizada após a alteração do elemento na posição 5
print(L)



# Define uma lista de números
L = [1, 2, 3, 4]
# Imprime o comprimento da lista (quantidade de elementos)
print(len(L))
# Imprime o menor valor na lista
print(min(L))
# Imprime o maior valor na lista
print(max(L))
# Imprime a soma de todos os valores na lista
print(sum(L))
# Verifica se o número 3 está presente na lista e imprime o resultado
print(3 in L)
# Define uma lista desordenada
L = [5, 7, 2, 9, 4, 1, 3]
# Ordena a lista em ordem crescente
L.sort()
print("Lista em ordem crescente: ", L)
# Inverte a ordem dos elementos na lista
L.reverse()
print("Inverte os elementos: ", L)

# Concatenação de listas
a = [0, 1, 2]  # Define a lista 'a'
b = [3, 4, 5]  # Define a lista 'b'
c = a + b      # Concatena as listas 'a' e 'b' para formar uma nova lista 'c'
print(c)      # Imprime a lista resultante da concatenação

# Repetição de elementos em uma lista
L = [1, 2]    # Define a lista 'L'
R = L * 4     # Repete os elementos da lista 'L' quatro vezes para formar uma nova lista 'R'
print(R)      # Imprime a lista resultante da repetição


# Listas com range
# Cria uma lista usando a função range(), que gera uma sequência de números de 0 até 4 (exclusivo)
L1 = list(range(5))
print(L1)  # Imprime a lista L1
# Cria uma lista usando a função range(), que gera uma sequência de números de 3 até 7 (exclusivo)
L2 = list(range(3, 8))
print(L2)  # Imprime a lista L2
# Cria uma lista usando a função range(), que gera uma sequência de números de 2 até 10, com um passo de 3
L3 = list(range(2, 11, 3))
print(L3)  # Imprime a lista L3


