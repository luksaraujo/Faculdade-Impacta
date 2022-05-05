def coleta_notas():
    notas = input().split()
    for i in range(len(notas)):
        notas[i] = float(notas[i])
    return notas

def preenche_turma(qtd_alunos):
    turma = []
    for i in range(qtd_alunos):
        print(f'{i + 1}º aluno:', end=' ')
        aluno = coleta_notas()
        turma.append(aluno)
    return turma

def calcula_media(aluno):
    soma = 0
    for nota in aluno:
        soma += nota
    return soma / len(aluno)

def resumo_turma(turma):
    for aluno in turma:
        media = calcula_media(aluno)
        print(f'notas: {aluno} | média: {media:5.2f}')

qtd_alunos = int(input('Quantidade: '))
turma = preenche_turma(qtd_alunos)
resumo_turma(turma)
