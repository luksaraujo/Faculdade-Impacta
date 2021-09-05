# Faça uma função que receba por parâmetro uma lista de reais e retorne o
# maior valor negativo encontrado na lista.Faça upload de arquivos com a
# solução do problema solicitado.

# --------------- Function ---------------
def higher_negative_value(reals_list):
    reals_list.sort()
    minor_element_found = None
    for element in reals_list:
        if element < 0:
            minor_element_found = element
        else:
            break
    return minor_element_found
# ----------------------------------------