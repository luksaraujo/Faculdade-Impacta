def maiorM(M):
    """
    Função maiorM
    Objetivo: Retorna o maior valor encontrado nessa matriz e uma lista com as posições onde ele é encontrado
    A lista de posições deve ser composta de tuplas com a linha, colluna onde o maior valor é encontrado
    Documentar a função como visto em aula
    """
    maior = M[0][0]
    nlinhas = len(M)
    for lin in range(nlinhas):
        for col in range(nlinhas):
            if M[lin][col] > maior:
                maior = M[lin][col]
    L1 = []
    for lin in range(nlinhas):
        for col in range(nlinhas):
            if M[lin][col] == maior:
                L1.append((lin,col))
    return maior, L1