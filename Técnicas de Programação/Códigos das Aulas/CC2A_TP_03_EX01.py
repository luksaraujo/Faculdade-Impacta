# Crie um função que receba como parâmetro uma matriz quadrada de
# inteiros e retorne a soma dos elementos de sua diagonal principal

def impdp(MAT):
    somador = 0
    nlinhas=len(MAT)
    ncolunas=len(MAT[0])
    for linha in range(nlinhas):
        for coluna in range(ncolunas):
            if linha==coluna:
                somador += MAT[linha][coluna]
    return somador
