vTotal = int(input())
vMensal = int(input())

vRestante = vTotal
contador = 1
while vRestante > 0:
    print('pagamento:', contador)
    print('antes =', vRestante)
    vRestante -= vMensal
    if(vRestante < 0):
        vRestante = 0
    print('depois =', vRestante)
    contador += 1
    print('-----')
