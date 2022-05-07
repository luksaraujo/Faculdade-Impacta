# Utilizando a biblioteca OS, criar um programa que:
# 1) Lista o nome do sistema operacional
# 2) Lista o nome da pasta atual
# 3) Lista os arquivos da pasta atual

import os
print(os.name)
print(os.getcwd())
os.listdir()