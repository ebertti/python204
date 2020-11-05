

# antes de executar este código, tente adivinhar a ordem dos prints em cada cenário

def gerador(qtd):
    print('10 antes')
    for i in range(qtd):
        print('20 para cada', i)
        yield i * 10

def normal(qtd):
    print('10 antes')
    lista = []

    for i in range(qtd):
        print('20 para cada', i)
        lista.append(i * 10)

    return lista

if __name__ == '__main__':

    print('1 main')
    #l = normal(2)
    l = gerador(2)
    print('2 depois do init')
    for i in l:
        print('3 fora', i)

# # troque entre normal(2) e gerador(2) para ver a diferença
#
#
# banco lista 1000000 (100k) -> filtra idade > 10 filtrar sexo masculino
#
# lista = consulta('sql') <- 1MM
# # 1MM * 100K
#
# lista_filtrada = []
#
# for item in lista:
#     if item.idade > 10:
#         lista_filtrada.append(item)
#
# lista_filtrada # 100MIL
# # total 1MM + 100M
#
#
# lista_masculina = []
#
# for item in lista_filtrada:
#     if item.sexo == 'masculino':
#         lista_masculina.append(item)
#
# lista_filtrada # 80MIL
# # total 1MM + 100M + 80M
#
# def query():
#     for linha in query('ququasdoashdoi').iterator():
#         print('query')
#         yield linha
#
# def idade(lista):
#     for item in lista:
#         print('idade')
#         if item.idade > 10:
#              yield item
#
# def sexo(lista):
#     for item in lista_filtrada:
#         print('sexo')
#         if item.sexo == 'masculino':
#             yield item
#
# q = query()
# q1 = idade(q)
# q2 = sexo(q1)
#
# for i in q2: # <- 'executado'
#     print('resultado')
#     print(i)
