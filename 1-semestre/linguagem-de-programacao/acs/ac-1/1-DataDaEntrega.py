dia = input()
prazo = int(input())

dias = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']

dayIndex = dias.index(dia)

dayIndex += prazo

if dayIndex > 6:
    dayIndex -= 7

entrega = dias[dayIndex]

if prazo == 0:
    print('chega hoje!')
else:
    print('sera entregue', entrega)
