'''
Em cada fase do jogo do Pula Sapo você deve conduzir
seu anfíbio através de uma sequência de canos de alturas
diferentes até chegar a salvo no cano mais à direita.
Entretanto, o sapo só consegue sobreviver se a diferença
de altura entre canos consecutivos for de, no máximo, a
altura do pulo do sapo. Caso a altura do cano seguinte
seja muito alta, o sapo bate no cano e cai. Se a altura
do cano seguinte for muito baixa, o sapo não aguenta a
queda. O sapo sempre começa em cima do cano mais à esquerda.

Neste jogo, a distância entre os canos é irrelevante, ou
seja, o sapo sempre consegue alcançar o próximo cano com
um pulo.



Você deve escrever um programa que, dadas as alturas dos
canos e a altura do pulo do sapo, mostra se a fase do jogo
pode ser vencida ou não.

Entrada
A entrada é dada em duas linhas. A primeira tem dois
inteiros positivos P e N, a altura do pulo do sapo e o número
de canos (1 ≤ P ≤ 5 e 2 ≤ N ≤ 100). A segunda linha tem N
inteiros positivos que indicam as alturas dos canos ordenados
da esquerda para a direita. Não há altura maior do que 10.

Saída
A saída é dada em uma única linha. Se o sapo pode chegar no
cano mais à direita, escreva "YOU WIN". Se o sapo não consegue,
escreva "GAME OVER".
'''

def entrada():                                                          # Cria a função que solicita as entradas
    altura_pulo, qtde_canos = map(int, input().split())                 # Coleta a altura do pulo e a qtde de canos
    alturas_canos = input().split()                                     # coleta a qtde de canos e separa os valores dentro da variável, tornando-a um vetor
    for i in range(len(alturas_canos)):                                 # laço da função que transforma as posições do vetor em números inteiros
        alturas_canos[i] = int(alturas_canos[i])                        # Converte os valores em inteiros e os adiciona em suas posições originais
    return altura_pulo, qtde_canos, alturas_canos                       # retorna os valores obtidos

def verifica(a, b, altura_pulo):                                        # cria a função que verifica se a altura do pulo é maior ou não do que o permitido
    if abs(a-b) > altura_pulo:                                          # Se o valor absoluto (remove o sinal negativo) de 'a-b' for maior do que a altura do pulo
        return True                                                     # retorna True
    else:                                                               # senão
        return False                                                    # retorna False

altura_pulo, qtde_canos, alturas_canos = entrada()                      # Preenche as variáveis com os valores coletados pela função 'entrada()'
a = False                                                               # Inicializa 'a' como 'False'
for i in range(qtde_canos-1):
    a = verifica(alturas_canos[i], alturas_canos[i+1], altura_pulo)     # Chama a função 'verifica' e armazena o retorno na variável 'a'
    if a == True:                                                       # Se 'a' for igual a verdadeiro
        print('GAME OVER')                                              # Imprime 'GAME OVER'
        break                                                           # sai do laço
if a == False:                                                          # Se 'a' for igual a falso
    print('YOU WIN')                                                    # Imprime 'YOU WIN'
