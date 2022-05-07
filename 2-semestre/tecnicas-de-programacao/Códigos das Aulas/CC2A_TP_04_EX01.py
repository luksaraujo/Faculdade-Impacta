def ex_01(texto, letra):
    var = 0
    for x in texto:
        if x == letra:
            var += 1
    return var

print(ex_01('banana', 'a'))