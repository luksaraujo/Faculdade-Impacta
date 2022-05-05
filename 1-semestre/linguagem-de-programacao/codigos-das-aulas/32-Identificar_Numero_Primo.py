'''
Na matemática, um Número Primo é aquele que pode ser
dividido somente por 1 (um) e por ele mesmo. Por exemplo,
o número 7 é primo, pois pode ser dividido apenas pelo
número 1 e pelo número 7.

Entrada
A entrada contém vários casos de teste. A primeira linha
da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando
o número de casos de teste da entrada. Cada uma das N
linhas seguintes contém um valor inteiro X (1 < X ≤ 107),
que pode ser ou não, um número primo.

Saída
Para cada caso de teste de entrada, imprima a mensagem
“X eh primo” ou “X nao eh primo”, de acordo com a
especificação fornecida.
'''

qtde_testes = int(input())

for i in range(0, qtde_testes):
    num = int(input())
    soma = 0
    j=1
    while j <= num:
        if num % j == 0:
            soma = soma + 1
        j = j + 1
    if soma > 2:
        print('{} nao eh primo'.format(num))
    else:
        print('{} eh primo'.format(num))
