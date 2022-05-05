vetor=[]
teste = int(input())
for a in range(teste) :
    falso=False
    matriz=[]
    for i in range(9) :
        matriz.append(list(map(int,input().split(" "))))
    for linha in matriz :
        for coluna in linha :
            if linha.count(coluna)>1 : falso=True
    for i in range(9) :
        x=[]
        for linha in matriz :
            if not(linha[i] in x) : x.append(linha[i])
        if len(x)!=9 :
            falso=True
    for linham in range(0,9,3) :
        x1=[]
        x2=[]
        x3=[]
        for linha in range(linham,linham+3) :
            for colunam in range(0,9,3) :
                for coluna in range(colunam,colunam+3) :
                    if colunam==0 :
                        if not(matriz[linha][coluna] in x1) : x1.append(matriz[linha][coluna])
                    if colunam==3 :
                        if not(matriz[linha][coluna] in x2) : x2.append(matriz[linha][coluna])
                    if colunam==6 :
                        if not(matriz[linha][coluna] in x3) : x3.append(matriz[linha][coluna])
        if len(x2)!=9 : falso=True
        if len(x3)!=9 : falso=True
        if len(x1)!=9 : falso=True
    vetor.append([])
    vetor[-1].append("Instancia " + str(a+1))
    if falso : vetor[-1].append("NAO")
    else : vetor[-1].append("SIM")
for i in vetor :
    print(i[0])
    print(i[1])
    print()
