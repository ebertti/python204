figuras = [
    {'nome': 'aaa', 'caracteristicas': [1, 2, 3]},
    {'nome': 'vvv', 'caracteristicas': [3, 2]},
    {'nome': 'bbb', 'caracteristicas': [5, 2, 1]},
    {'nome': 'ttt', 'caracteristicas': [6, 1, 6, 7, 8]},
]

for figura in figuras:
    # figurinha é um dicionario
    print(figura['nome'])
    for caracteristica in figura['caracteristicas']:
        print(caracteristica)
