'''
Você está criando um site para uma loja virtual e precisa guardar os itens que os usuários
adicionam em seu carrinho. Cada item é representado no sistema por um código numérico, isto
é, um número inteiro que é capaz de identificá-lo unicamente. Como solução inicial, você
decidiu guardar os itens adicionados ao carrinho em uma lista, e para testar o seu programa,
implementou alguns comandos básicos para simular uma interação do usuário com o sistema:

adicionar: inclui o código de um novo produto à lista;
remover: remove o código de um produto da lista;
exibir: exibe os itens da lista em ordem crescente;
encerrar: exibe os itens da lista, assim como no comando exibir, em ordem crescente, e encerra
o programa.

A primeira linha poderá conter uma lista de inteiros separados por espaços, representando
produtos que já estavam no carrinho, por exemplo, de uma sessão anterior que o usuário iniciou
mas não finalizou a compra. Você deve receber essa lista e inicializar o carrinho de compras
já com os códigos dessa lista, que devem ser números inteiros.

Caso não haja nenhum produto salvo de uma sessão anterior, essa primeira linha será uma linha em
branco, sem nenhum texto ou caractere.

Entrada
A primeira linha poderá conter números inteiros separados por espaço ou ser uma linha em branco;
Cada linha seguinte conterá um dos comandos listados acima e, para os comandos "adicionar" e
"remover", conterá também o código de um produto separado por um espaço;

A entrada termina sempre com o comando "encerrar".

Saída
A saída deve conter:
A exibição dos códigos na lista, separados por espaço, de acordo com a execução dos comandos
"exibir" e "encerrar";

A mensagem "código <código> não encontrado", quando o comando remover é executado com um código
que não esteja presente na lista. Substitua <código> pelo número do código em questão (veja os
exemplos para maiores detalhes).
Obs.: Lembre-se de não exibir texto no input.
'''

''' -------------------- VARIÁVEIS DO PROGRAMA -------------------- '''
lista_de_produtos = []                                  #Inicializa a lista de produtos como um vetor vazio
tamanho_do_vetor = 0                                    #Inicializa a variável responsável por armazenar os tamanhos dos vetores
''' --------------------------------------------------------------- '''

''' --------------------- FUNÇÕES DO PROGRAMA --------------------- '''
def remover_produto(produto):                           #Inicializa a função 'remover_produto'
    if produto in lista_de_produtos:                    #Se o parâmetro 'produto' existe na 'lista_de_produtos'
        indice = lista_de_produtos.index(produto)       #Armazena o índice do produto da lista de produtos na variável 'indice'
        del(lista_de_produtos[indice])                  #Remove o índice equivalente ao produto da lista_de_produtos
    else:                                               #Se o parâmetro 'produto' não existe na 'lista_de_produtos'
        print(f'código {produto} não encontrado')       #Informa que o código não foi encontrado

def adicionar_produto(produto):                         #Inicializa a função 'adicionar_produto'
    lista_de_produtos.append(produto)                   #Insere o parâmetro passado para a função na lista de produtos

def exibir_lista(lista):                                        #Inicializa a função 'exibir_lista'
    lista_ordenada = sorted(lista)                              #Ordena de forma crescente o parâmetro que foi passado na execução da função e armazena na variável 'lista_ordenada'
    string = ' '.join([str(item) for item in lista_ordenada])   #Insere cada item da 'lista_ordenada' dentro da variável 'string', mas como se fosse uma frase e não um vetor, separando-os por espaços
    print(string)                                               #Exibe a variável 'string'

def primeira_leitura():                                     #Inicializa a função 'primeira_leitura'
    entrada_inicial = input().split()                       #Lê os valores e os armazena no vetor 'entrada_inicial'
    if entrada_inicial != []:                               #Se a entrada inicial for diferente de 'vazio'
        entrada_inicial = list(map(int, entrada_inicial))   #Converte o vetor de str para int
        tamanho_do_vetor = len(entrada_inicial)             #Armazena o tamanho do vetor 'entrada_inicial' na variável
        for i in range(tamanho_do_vetor):                   #For
            lista_de_produtos.append(entrada_inicial[i])    #Insere os itens informados na lista de produtos
''' --------------------------------------------------------------- '''

''' ---------------------- CÓDIGO DO PROGRAMA ---------------------- '''
primeira_leitura()                                          #Executa a função 'primeira_leitura'
while True:                                                 #Loop que faz com que o programa sempre peça um input ao usuário
    comando = input()                                       #Armazena na variável 'comando' o que o usuário digitar
    if comando == 'exibir':                                 #Se o comando digitado for 'exibir'
        exibir_lista(lista_de_produtos)                     #Executa a função 'exibir_lista' e passa a variável / vetor lista_de_produtos como parâmetro
    elif comando.split(" ")[0] == 'adicionar':              #Divide a string informada pelo usuário no espaço e compara se a primeira palavra é 'adicionar'. Se sim:
        adicionado = int(comando.split(" ")[1])             #Armazena o segundo caractere do comando já convertido em um número inteiro na variável 'adicionado'
        adicionar_produto(adicionado)                       #Chama a função 'adicionar_produto' e passa a variável 'adicionado' como parâmetro
    elif comando.split(" ")[0] == 'remover':                #Divide a string informada pelo usuário no espaço e compara se a primeira palavra é 'remover'. Se sim:
        removido = int(comando.split(" ")[1])               #Armazena o segundo caractere do comando já convertido em um número inteiro na variável 'removido'
        remover_produto(removido)                           #Chama a função 'remover_produto' e passa a variável 'removido' como parâmetro
    else:
        exibir_lista(lista_de_produtos)                     #Executa a função 'exibir_lista' e passa a variável / vetor lista_de_produtos como parâmetro
        break                                               #Sai do loop infinito, encerrando o programa
''' ---------------------------------------------------------------- '''
