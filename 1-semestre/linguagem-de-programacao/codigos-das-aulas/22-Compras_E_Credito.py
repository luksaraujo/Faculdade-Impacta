credito = float(input('Seu crédito: '))
total = 0
i=1
preco = float(input('Preço do item 1: '))
while credito >= preco:
    total += preco
    credito -= preco
    i += 1
    preco = float(input(f'Preço do item {i}: '))
print(f'Compra do item {i} negada')
print(f'Itens comprados: {i-1}')
print(f'Total da compra é R$ {total:.2f}')
print(f'Crédito restante é R$ {credito:.2f}')
