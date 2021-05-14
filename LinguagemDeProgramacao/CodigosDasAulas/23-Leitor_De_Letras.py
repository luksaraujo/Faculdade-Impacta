letra = input('Digite uma letra: ')
letra = letra.upper()
contador = 0
while letra != 'X':
    contador += 1
    letra = input('Digite mais uma letra: ')
    letra = letra.upper()
print(f'Quantidade de letras lidas: {contador}')
