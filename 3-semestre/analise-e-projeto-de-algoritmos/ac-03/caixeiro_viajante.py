from itertools import permutations
import random

# Função usada para calcular raiz quadrada
from math import sqrt

# Módulo usado apenas na geração dos gráficos para facilitar a visualização da solução
import matplotlib.pyplot as plt 

# Gerar as coordenadas aleatoriamente
def randomCoordenates(length):
    coordenates = []
    while True:
        coordenate = []
        for j in range(2):
            coordenate.append(random.randint(1, 10))
        if not coordenate in coordenates:
            coordenates.append(coordenate)
        if len(coordenates) == length:
            break
    return coordenates

#Soma de dois pontos
def matrixSum(pontoA, pontoB):

  #Aplicação da fórmula de distância entre dois pontos
  distancia = (((pontoB[0] - pontoA[0]) * 2 ) + ((pontoB[1] - pontoA[1]) * 2))

  #Dado por D = sqrt(Bx - Ax)^2 + ((By - Ay)^2))
  distancia = sqrt(abs(distancia))

  # Retorna a distância entre os dois pontos dados
  return distancia

def sumFloat(lst):
  sum = 0
  for i in range(len(lst)):
    sum += lst[i]
  return sum

def executarCarixeiro(qtde_cidades):
  #Array que guardará todas as coordenadas do imput
  coordMatrix = randomCoordenates(qtde_cidades)

  #Lista que armazena a soma das iterações entre os pontos das coordenadas dada a permutação.
  #É dado um .clear() quando se coloca outra permutação, já que é outra soma
  pontosCalc = []

  #Array que vai guardar o resultado de TODAS as permutações e no final, será retirado o menor do array, que é a menor distância que o caixero percorrerá
  somasPossiveis = []

  #Dicionário que armazena a distância percorrida e as coordenadas em chave e valor respectivamente
  somaCoord = {}

  #Loop para transformar todos os elementos em inteiros
  for i in range(len(coordMatrix)):
      for j in range(2):
          (coordMatrix[i][j]) = int(coordMatrix[i][j])
  print(f"Coordenadas das cidades a serem visitadas: {coordMatrix}")

  #coordPermut armazena todas as permutações das coordenadas mas é só permut que consegue percorrer entre as combinações
  coordPermut = permutations(coordMatrix)

  for permut in (coordPermut):
      for i in range(len(permut) - 1):
          
          #Coloca cada combinação da coordenada e a próxima para ser somado na função que calcula a distância entre doois pontos
          sum = matrixSum(permut[i], permut[i + 1])
          
          #Depois de calculada, a distância entre somente dois pontos numa lista
          pontosCalc.append(sum)
      
      #Após o termino de colocar a distância de todos os pontos, é necessário somá-los, para que assim se tenha a distância total do trajeto daquela combinação
      somaCalc = sumFloat(pontosCalc) #Aqui, soma-se todas as coordenadas
      somasPossiveis.append(somaCalc) #E então, armazena-se num array onde terão todas as distâncias de todas as permutações
      
      #Neste dicionário, se guardarâo a coordenada junto com a soma da trajetória
      somaCoord.update({str(somaCalc) : str(permut)})
      
      #Aqui, limpa-se o array para que seja possível armazenar a soma das coordenadas de outras combinações
      pontosCalc.clear()

  # print(f"A menor distancia que o caixeiro pode percorrer dentre as coordenadas apresentadas é {min(somasPossiveis)}")
  menorValor = str(min(somasPossiveis))
  print(f"Ordem de visitação das coordenadas: {somaCoord.get(menorValor)}")

  #Neste array, pega-se a coordenada da menor distância possível a se percorrer no dicionário 'somaCoord', e transforma a string em uma lista
  coordMelhorCaminho = str(somaCoord.get(menorValor)).replace("(","").replace(")","").replace("[","").replace("]","").replace(",", "").split()

  #Como ele é armazenado como string, é necessário fazer a conversão para inteiros
  coordMelhorCaminho = list(map(int, coordMelhorCaminho))

  #Nesta lista, armazena-se as coordenadas para futaramente construir os gráficos
  coordPlot = []

  #Variável auxiliar para poder acessar os elementos de 'coordMelhorCaminho' e poder indexá-los em um array de 2 dimensões
  count = int(0)

  #Pelo fato de que quando o array foi construido ele foi colocado em 1D, a intenção é fazer um de 2D, e para isso
  #o novo array terá metade dos indicies do anterior, por isso, //2
  for index in range((len(coordMelhorCaminho)//2)): 
      
      #Aqui, pega-se um elemento da lista 1D 'coordMelhorCaminho' e o próximo elemento a fim de colocar os dois elementos NO MESMO ÍNDICE, na lista coordPlot
      coordPlot.append([coordMelhorCaminho[count], coordMelhorCaminho[count + 1]])
      
      #Acrescenta-se 2 à count pois já que pegamos o count e count + 1, para não pegarmos um elemento repetido, precisa-se pegar (count + 1) + 1, ou seja, 2
      count += 2

  #Por fim, temos uma lista de 2 dimensões com a melhor coordenada pela qual o Caixeiro pode percorrer

  #---------------------------Plotagem de Gráficos-----------------

  x_plt = []
  y_plt = []

  print(coordPlot.append(coordPlot[0]))
  print(coordPlot)
  for i in range(len(coordPlot)):    
          x_plt.append(coordPlot[i][0])
          y_plt.append(coordPlot[i][1])
  ax = plt.plot(x_plt, y_plt, label="Trajetória do caixeiro")
  plt.xlim(0, int(max(somasPossiveis)))
  plt.ylim(0, int(max(somasPossiveis)))
  plt.legend()
  plt.show()
  print("--------------------------------------------------------")

#%time
executarCarixeiro(4)
