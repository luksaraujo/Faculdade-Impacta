'''
Na matemática, um número perfeito é um número
inteiro para o qual a soma de todos os seus
divisores positivos próprios (excluindo ele mesmo)
é igual ao próprio número. Por exemplo o número 6
é perfeito, pois 1+2+3 é igual a 6. Sua tarefa é
escrever um programa que imprima se um determinado
número é perfeito ou não.

Entrada
A entrada contém vários casos de teste. A primeira
linha da entrada contém um inteiro N (1 ≤ N ≤ 20),
indicando o número de casos de teste da entrada.
Cada uma das N linhas seguintes contém um valor
inteiro X (1 ≤ X ≤ 108), que pode ser ou não, um
número perfeito.

Saída
Para cada caso de teste de entrada, imprima a
mensagem “X eh perfeito” ou “X nao eh perfeito”,
de acordo com a especificação fornecida.
'''

qtde_casos = int(input())
for contador1 in range(0, qtde_casos):
    numero = int(input())
    contador2 = 1
    soma = 0
    while contador2 < numero:
        if numero % contador2 == 0:
            soma += contador2
        contador2 += 1
    if soma == numero: 
        print(f'{numero} eh perfeito')
    else:
        print(f'{numero} nao eh perfeito')
