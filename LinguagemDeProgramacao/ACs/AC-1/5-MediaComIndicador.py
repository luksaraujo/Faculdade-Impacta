trabalhos = float(input())
prova = float(input())
nota_final = (trabalhos + prova) / 2

if nota_final >= 6:
    print('aprovado')
else:
    media_sub = 10
    nota_final = (media_sub + nota_final) / 2
    if nota_final > 6:
        print('talvez com sub')
    else:
        print('reprovado')
