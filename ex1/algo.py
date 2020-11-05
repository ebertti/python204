"""
o(1)      - hash
o(logn)   - busca rapida (coleção ordenada)
o(n)      - busca simples
o(nlogn)  - ordenação rapida
o(2n)
o(n2)    - ordenação lenta
o(n^n)
"""

def exemplo1():

    # if in é o(n)
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    ## ifs in é o(1)
    colecao = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    dicionario = {'a': 0, 'b':2}


    # com indice no banco #keyscan
    # 2 ** x = 1024
    # 10 interaçoes

    # sem indice (100x mais lento) #fullscan
    # 1024 interaçoes






