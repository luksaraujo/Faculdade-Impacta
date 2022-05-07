# Crie um função que receba como parâmetro uma matriz de
#  inteiros e um número N e retorne uma lista com todos
#  os valores da matriz que são maiores que N

def impdp(MAT, N):
    maiores_que_N = []
    nlinhas=len(MAT)
    ncolunas=len(MAT[0])
    for linha in range(nlinhas):
        for coluna in range(ncolunas):
            if MAT[linha][coluna] > N:
                maiores_que_N.append(MAT[linha][coluna])
    return maiores_que_N
