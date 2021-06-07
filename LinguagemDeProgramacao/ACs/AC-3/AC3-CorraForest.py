'''
Forrest é um garoto que adora correr e contar histórias,
as vezes até conta histórias sobre correr... vai entender.
Como costuma correr diariamente pela cidade, Forrest sempre
procura fazer o menor tempo possível, porém não é muito
organizado e anota os tempos de suas corridas em papeis que
são jogados em sua gaveta sem nenhum tipo de ordenação.

Como Forrest está muito ocupado ultimamente, planejando como
cumprir uma promessa a um antigo amigo que adorava restaurantes
e camarão, pediu a você que crie um programa que receba como
entrada os tempos das corridas que estão nos papeis e calcule
a média aritmética dos tempos gastos por Forrest para completar
o seu percurso de corrida diário. Ao final, seu programa deve
também exibir todos os tempos que ficaram abaixo dessa média, na
mesma ordem em que foram recebidos na entrada.

Entrada
Diversos valores inteiros, um por linha, que representam os tempos
gastos em cada corrida (em segundos);

A entrada é finalizada com a inserção de um valor negativo, que não
deve ser contabilizado.

Saída
Na primeira linha a palavra 'MEDIA', sem apóstrofos, sem acentuação e
completamente em maiúsculo, seguida por dois pontos (':'), um caractere
de espaço e um valor real com duas casas decimais, indicando a média dos
tempos dados na entrada, em segundos;

Nas linhas seguintes, os tempos que ficaram abaixo dessa média, em
segundos, um por linha.
'''

''' -------------------- VARIÁVEIS DO PROGRAMA -------------------- '''
lista_tempos = []                                                   #Inicializa o vetor que armazenará os tempos de cada corrida
''' --------------------------------------------------------------- '''

''' --------------------- FUNÇÕES DO PROGRAMA --------------------- '''
def exibir_resultado():                                             #Inicializa a função que exibe o resultado final do programa
    media = 0                                                       #Inicializa a variável que armazenará a média de tempo da corrida
    for i in range(0, len(lista_tempos)):                           #Estrutura de repetição responsável por somar todos os tempos do vetor
        media += lista_tempos[i]                                    #Soma todos os valores na variável 'media'
    media = media / len(lista_tempos)                               #Calcula a média dos tempos
    print(f'MEDIA: {media:.2f}')                                    #Exibe a média
    for j in range(0, len(lista_tempos)):                           #Estrutura de repetição responsável por exibir os valores menores do que a média
        if lista_tempos[j] < media:                                 #Se o valor que estiver sendo lido for menor do que a média
            print(lista_tempos[j])                                  #Exibe o valor

def popular_vetor(tempo, lista):                                    #Inicializa a função que populará o vetor que contém os tempos das corridas
    lista.append(tempo)                                             #Insere o valor informado pelo usuário na última posição do vetor que armazena os tempos das corridas
''' --------------------------------------------------------------- '''

''' ---------------------- CÓDIGO DO PROGRAMA ---------------------- '''
while True:                                                         #Faz com que o programa sempre esteja em loop infinito, até que um 'break' seja lido
    tempo_corrida = int(input())                                    #Variável que armazena o tempo gasto na corrida, já convertido para int
    if tempo_corrida < 0:                                           #Se o valor lido for menor do que zero (negativo)
        exibir_resultado()                                          #Chama a função exibir resultado
        break;                                                      #Sai do loop infinito
    else:                                                           #Se o valor lido não for negativo
        popular_vetor(tempo_corrida, lista_tempos)                  #Chama a função que insere o valor no vetor, passando o dado informado pelo usuário e o vetor como parâmetro
''' ---------------------------------------------------------------- '''
