
a = [1, 2, 3, 4, 5, 6, 7]
a.append(1)
a.append(2)

a.remove(1)  # valor
a.pop()      # posicao

a.insert(2, 1)

a[::-2]

nome = 'Ezequiel'
nome[1:]


# qtd numeros === infome uma qtd de numeros
# obter essa qtd de numeros === informar cada numero

lista = []
qtd = int(input('quantidade'))
for i in range(qtd):
    lista.append(int(input('valor')))

print(sum(lista))
