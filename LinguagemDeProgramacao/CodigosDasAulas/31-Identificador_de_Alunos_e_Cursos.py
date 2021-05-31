'''
Roberto precisava coletar o numero de matricula
dos alunos da sua turma de engenharia de produção
e engenharia hídrica para a chamada. Logo, ele
teve a excelente ideia de falar para todos os seus
alunos gritarem os números de chamada para seus
assistentes anotarem. Obviamente, isso não deu certo,
e logo a sala entrou em colapso. Todos queriam falar
ao mesmo tempo, e com a competição para ver quem
conseguia ir embora mais rápido, houve um principio
de tumulto, com cadeiras sendo jogadas nos colegas,
puxões de cabelo, e socos na cara.

Júnior como é um cara pacífico, está tentando atender
todos rapidamente. Porem, como são muitas requisições,
está ficando sobrecarregado. Ele então, lembrou que você
sabe programar e decidiu dar uma ideia.

Todos os alunos da sala deverão dar os nomes de matricula
e a sigla do curso em uma folha, e a chamada sera
computada posteriormente. Ele precisa saber quantos alunos
de cada curso compareceram. Ele tem os dados, mas infelizmente,
não tem a proeficiencia necessária em programação para “codar”
isso. Você poderia ajuda-lo a saber, dada uma lista de alunos,
quantos são de EPR, quantos são de EHD e quantos são intrusos?

Entrada
A primeira linha da entrada um inteiro n ( 1<=n<=100000 ) que
indicam o numero de alunos na sala.

As n linhas seguintes contem o numero de matricula e a sigla
do curso.

A leitura do programa deve acabar com fim de arquivo.

Saída
Seu programa deve imprimir 3 linhas contendo o numero de alunos
que são de EPR, EHD, e INTRUSOS no formato: “sigla: quantidade”.
( Ver exemplo de saída ).
'''

while True:
    try:
        qtde_alunos_presentes = int(input())
        epr = 0 # Quantidade de alunos de EPR
        ehd = 0 # Quantidade de alunos de EHD
        intrusos = 0 # Quantidade de alunos intrusos
        for i in range(qtde_alunos_presentes):
            matricula, curso = input().split()
            if curso == 'EPR':
                epr += 1
            elif curso == 'EHD':
                ehd += 1
            else:
                intrusos += 1
        print(f'EPR: {epr}')
        print(f'EHD: {ehd}')
        print(f'INTRUSOS: {intrusos}')
    except EOFError:
        break
