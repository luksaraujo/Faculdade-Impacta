# Considerando a entrada de valores inteiros não negativos, ordene estes valores segundo o seguinte critério:

# Primeiro os Pares
# Depois os Ímpares
# Sendo que deverão ser apresentados os pares em ordem crescente e depois os ímpares em ordem decrescente.

# Entrada
# A primeira linha de entrada contém um único inteiro positivo N (1 < N <= 105) Este é o número de linhas de
# entrada que vem logo a seguir. As próximas N linhas conterão, cada uma delas, um valor inteiro não negativo.

# Saída
# Apresente todos os valores lidos na entrada segundo a ordem apresentada acima. Cada número deve ser impresso
# em uma linha, conforme exemplo abaixo.

qtt_tests = int(input())
inserted_numbers = []
pair_numbers = []
odd_numbers = []
for i in range(qtt_tests):
    number = int(input())
    inserted_numbers.append(number)
inserted_numbers.sort()
for number in inserted_numbers:
    if number % 2 == 0:
        pair_numbers.append(number)
    else:
        odd_numbers.append(number)
for number in pair_numbers:
    print(number)
odd_numbers.sort(reverse = True)
for number in odd_numbers:
    print(number)