
tupla = (1, 2, 3, 4)

lista = [2, 3, 4, 5]


lista = []
lista.append('Ezequiel')
lista.append('João')
lista.append('Jose')
lista.append('Thales')
lista.append('leao')
lista.remove('Ezequiel')
lista.pop(0)
lista.pop(1)
lista.pop()
lista.append('Ezequiel')
lista.append('Maria')
lista.append('Ana')
lista.append('Talita')
lista.append('Python')
lista.append('Pycharm')
lista.insert(3, 'Valor')
lista.insert(0, 'Primeiro')
lista.insert(-2, 'penultimo')
lista.insert(-1, 'penultimo')
len(lista)

len(lista) -1

lista.insert(-1, 'aaaaaaaaaaa')


def meu_range(entrada):
    i = 0
    while i < entrada:
        yield i
        i += 1

for i in range(10):
    print(i)

# output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

for i in range(5, 10):
    print(i)

# output: 5, 6, 7, 8, 9

for i in range(5, 10, -1):
    print(i)

# output: []

for i in range(10, 5, -1):
    print(i)

# output: 10, 9, 8, 7, 6


for i in range(0, 10, 3):
    print(i)

# A output 3, 6, 9
# B output 0, 3, 6, 9  <----
# C output 0, 4, 7
# D output 0, 2, 5, 8
