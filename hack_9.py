"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    contador = 0
    listaNueva = []
    result = [1,2,3]
    while contador < len(result):
        listaNueva.append(result[contador])
        listaNueva.append('@')
        contador += 1
    return listaNueva