import math
def eh_primo(n):
    raiz = int(math.sqrt(n))
    if n == 1:
        return False
        
    for i in range(2, raiz + 1):
        if n % i == 0:
            return False
    return True

start = int(input())
end = int(input())

nPrimos = 0
for x in range(start, end + 1):
    if eh_primo(x):
        print(x)
        nPrimos += 1

print('primos:', nPrimos)
