def maior_numero(n1, n2):
    error = "Os números são idênticos"
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return error
