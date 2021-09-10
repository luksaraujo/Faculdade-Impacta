# Crie um função que receba como parâmetro uma matriz de inteiros e 
# um número N e retorne a True se N existir na matriz e False se não existir

def impdp(MAT, N):
    nlinhas=len(MAT)
    ncolunas=len(MAT[0])
    for linha in range(nlinhas):
        for coluna in range(ncolunas):
            if MAT[linha][coluna] == N:
                return True
    return False
