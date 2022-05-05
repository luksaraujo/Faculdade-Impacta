loop = True
coins = list()
while loop:
    coin = float(input())
    if coin != -1:
        coins.append(coin)
    else:
        loop = False

sCoins = 0
sReal = 0
for coin in coins:
    sCoins += coin
    sReal += coin * 2.5

print('VC$ ' + '{0:.2f}'.format(sCoins))
print('R$ ' + '{0:.2f}'.format(sReal))
