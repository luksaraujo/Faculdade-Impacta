'''

Escreva um programa que receba como entrada dois números inteiros quaisquer
A e B e exiba todas as tabuadas existentes no intervalo fechado crescente
[ A..B ].

Entrada

Dois números inteiros, um em cada linha.

Saída

As tabuadas de todos os valores inteiros no intervalo fechado crescente
[ A..B ]. Ao fim de cada tabuada, exibir uma linha com dez hifens ('-').
Caso A seja maior do que B, o intervalo será vazio e, neste caso, deve
ser exibida somente a frase 'Nenhuma tabuada no intervalo!', sem
apóstrofos. Obs.: Lembre-se de não exibir texto no input.

'''

''' -------------------- VARIÁVEIS DO PROGRAMA -------------------- '''
primeiro_numero = int(input())                                              #Lê o primeiro número e o converte de string para int
segundo_numero = int(input())                                               #Lê o segundo número e o converte de string para int
''' --------------------------------------------------------------- '''

''' --------------------- FUNÇÕES DO PROGRAMA --------------------- '''
def exibir_tabuadas(num1, num2):                                            #Inicializa a função 'exibir_tabuadas'
    if num1 > num2:                                                         #Se o primeiro número for maior do que o segundo número
        print('Nenhuma tabuada no intervalo!')                              #Exibe a mensagem entre aspas simples
    else:                                                                   #Senão
        tabuada_feita = num1 - 1                                            #Cria a variável 'tabuada_feita', indicando a tabuada que acabou de ser feita (neste caso, vale o primeiro numero menos 1 porque a tabuada do primeiro número ainda não foi feita)
        tabuada_fazendo = num1                                              #Cria a variável 'tabuada_fazendo' e armazena o valor do num1, que equivale à tabuada que está sendo feita no momento
        while tabuada_feita != num2:                                        #Enquanto 'tabuada_feita' valor um número diferente do segundo parâmetro
            for i in range(1, 11):                                          #Faz dez vezes o que está dentro do 'for' (11 porque o 'for' descarta o último valor, que é 11)
                print(f'{tabuada_fazendo} x {i} = {tabuada_fazendo * i}')   #Imprime: "o valor de 'tabuada_fazendo' vezes o valor de 'i' igual a multiplicação de 'tabuada_fazendo' por 'i'
            print('----------')                                             #Exibe '----------' ao final de cada tabuada
            tabuada_fazendo += 1                                            #Incrementa 1 no valor de 'tabuada_fazendo'
            tabuada_feita += 1                                              #Incrementa 1 no valor de 'tabuada_feita'
''' --------------------------------------------------------------- '''

''' ---------------------- CÓDIGO DO PROGRAMA ---------------------- '''
exibir_tabuadas(primeiro_numero, segundo_numero)                            #Chama a função 'exibir_tabuadas', passando os valores das variáveis entre parênteses
''' ---------------------------------------------------------------- '''
