# Flores Florescem da França
# Criar um programa com uma função que verifica se a frase digitada é ou não um tautograma,
# retornando Y caso sim e N caso não.

def tautogram_reader(phrase):
    phrase = phrase.lower()
    words = phrase.split(' ')
    if len(words) == len([i for i in words if i[0] == phrase[0]]):
        return 'Y'
    else:
        return 'N'
    
frase = input("Digite a frase: ")
print(tautogram_reader(frase))