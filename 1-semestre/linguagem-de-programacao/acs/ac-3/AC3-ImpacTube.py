loops = int(input())

canais = []
for i in range(loops):
    canais.append(input().split(';'))

bonusPremium = float(input())
bonusNormal = float(input())

print('-----')
print('BÔNUS')
print('-----')

for canal in canais:
    bonus = 0
    if(canal[3] == 'sim'):
        bonus = bonusPremium
    else:
        bonus = bonusNormal

    value = ((float(canal[1])//1000) * bonus) + float(canal[2])

    print(f'{canal[0]}: R$ {value:.2f}')