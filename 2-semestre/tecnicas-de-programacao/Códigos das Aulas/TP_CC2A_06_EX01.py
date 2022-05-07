# Utilizando a função dir listar as funções do modulo math e cmath
# Esses módulos possuem funções com o mesmo nome? Se possuem quais são essas funções?

import math
import cmath

print("\nFunções e variáveis do módulo MATH:")
print(dir(math), "\n")
print("\nFunções e variáveis do módulo CMATH")
print(dir(cmath), "\n")

print("Todas as funções do módulo 'CMATH' existem no módulo 'MATH', exceto as seguintes:")
print("infj, nanj, polar, rect, phase")
