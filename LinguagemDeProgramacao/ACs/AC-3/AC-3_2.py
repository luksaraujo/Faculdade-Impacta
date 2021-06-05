x = int(input())
y = int(input())
i = 0
cont_bomdia = 0
cont_boatarde = 0
while i < x:
    #print(f'{i+1} bom dia')
    cont_bomdia += 1
    j = 0
    while j < y:
        #print(f'{j+1} boa tarde')
        cont_boatarde += 1
        j += 1
    i += 1
print('boa noite')
print(f'Bom dias: {cont_bomdia}')
print(f'Boa tardes: {cont_boatarde}')
