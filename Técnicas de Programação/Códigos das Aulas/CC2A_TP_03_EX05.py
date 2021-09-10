# Crie um função que receba como parâmetro uma matriz de 
# inteiros e um número N e retorne a soma de todos os valores 
# que estão na matriz e que são maiores que N

def blevers(MAT, N):
    soma_maiores_que_N = 0
    nlinhas=len(MAT)
    ncolunas=len(MAT[0])
    for linha in range(nlinhas):
        for coluna in range(ncolunas):
            if MAT[linha][coluna] > N:
                soma_maiores_que_N += MAT[linha][coluna]
    return soma_maiores_que_N
