num = int(input())

ant = 0
suc = 0
if (num % 2) == 0:
    ant = num - 1
    suc = num + 2 
else:
    ant = num - 2
    suc = num + 1

print(ant, suc)
