numero1 = int(input())
numero2 = int(input())
numero3 = int(input())
numero4 = int(input())
numero5 = int(input())
qtdePares = 0

if(numero1 % 2) == 0:
    qtdePares += 1
if(numero2 % 2) == 0:
    qtdePares += 1
if(numero3 % 2) == 0:
    qtdePares += 1
if(numero4 % 2) == 0:
    qtdePares += 1
if(numero5 % 2) == 0:
    qtdePares += 1

print(f'{qtdePares} valores pares')
