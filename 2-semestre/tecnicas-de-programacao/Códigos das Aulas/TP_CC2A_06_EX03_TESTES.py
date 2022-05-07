'''
Para o enunciado abaixo elabore APENAS 3 TESTES UNITÁRIOS (Apenas o Plano) como visto em aula para verificar se o seu programa esta correto
Elaborar um função que recebe como parâmetro uma Matrix de inteiros 3 x 3 e:
Retorna True se a soma dos elementos de sua diagonal principal for par
Retorna False a soma dos elementos de sua diagonal principal for impar

MATRIZ      RETORNO
1 2 3       False
4 5 6
7 8 9

MATRIZ      RETORNO
1 2 3       True
4 6 6
7 8 9

MATRIZ      RETORNO
12 17 32    True
42 61 63
17 18 09

'''

def valida(M):
    s = 0
    nlinhas = len(M)
    for i in range(nlinhas):
        s += M[i][i]
    if s % 2 == 0:
        return True
    else:
        return False

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3], [4, 6, 6], [7, 8, 9]]
m3 = [[12, 17, 32], [42, 61, 63], [17, 18, 9]]

print("TESTE PARA ", m1)
print(valida(m1))
print("Resultado esperado: False")

print("TESTE PARA ", m2)
print(valida(m2))
print("Resultado esperado: True")

print("TESTE PARA ", m3)
print(valida(m3))
print("Resultado esperado: True")