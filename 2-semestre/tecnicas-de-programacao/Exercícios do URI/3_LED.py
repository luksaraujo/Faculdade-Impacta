# João quer montar um painel de leds contendo diversos números. Ele não possui muitos leds, e não tem certeza se conseguirá
# montar o número desejado. Considerando a configuração dos leds dos números abaixo, faça um algoritmo que ajude João a descobrir
# a quantidade de leds necessário para montar o valor.
#
# Entrada
# A entrada contém um inteiro N, (1 ≤ N ≤ 1000) correspondente ao número de casos de teste, seguido de N linhas, cada linha contendo
# um número (1 ≤ V ≤ 10100) correspondente ao valor que João quer montar com os leds.
#
# Saída
# Para cada caso de teste, imprima uma linha contendo o número de leds que João precisa para montar o valor desejado, seguido da palavra "leds".

def qtt_leds(number):
    if number == "1":
        return 2
    elif number == "2" or number == "3" or number == "5":
        return 5
    elif number == "4":
        return 4
    elif number == "6" or number == "9" or number == "0":
        return 6
    elif number == "7":
        return 3
    elif number == "8":
        return 7

qtt_tests = int(input())
for i in range(qtt_tests):
    value = input()
    somador = 0
    for j in value:
        somador += qtt_leds(j)
    print(f'{somador} leds')