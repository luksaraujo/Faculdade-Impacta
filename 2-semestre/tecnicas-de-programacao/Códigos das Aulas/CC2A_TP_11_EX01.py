# Implemente uma função chamada ordemc que recebe uma lista como parâmetro e retorna
# True caso a lista esteja ordenada em ordem crescente e False caso contrário

def ordemc(lista):
	
	if sorted(lista) == lista:
		return True
	else:
		return False

lista_1 = [1, 2, 3, 4, 10, 20, 30]
lista_2 = [30, 20, 10, 4, 3, 2, 1]
	
print(ordemc(lista_1))