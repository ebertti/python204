#%% if simples
valor = input("informe um valor: ")

valor = int(valor)

if valor >= 10:
    print('o valor é maior que 10')

else:
    print('menor que 10')


#%% rodovia tem limite de 110 por hora.
# 55 limite minimo

velocidade = int(input('velocidade'))
if velocidade > 110:
    print('multado grave')
else:
    if velocidade < 55:
        print('multa leve')
    else:
        print('nao multado')

#%% ternario
a = 9
# em js:    resultado = a > 10 ? 'maior' : 'menor'
resultado = 'maior' if a > 10 else 'menor'
# resultado = 'maior' SE a > 10 SENAO 'menor'


#%% exemplo elif

velocidade = int(input('velocidade'))
if velocidade > 110:
    print('multado grave')
elif velocidade < 55:
    print('multa leve')
else:
    print('nao multado')


#%% 3 maneiras de executar um loop de 0 a 9
a = 0
while a < 10:
    print(a)
    a += 1

# for(i = 0; i < 10; i++){
#    EM JavaScript
# }

for i in range(10):
    print(i)


#%% for em uma lista
lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item)


#%% lista multiplicar por 3

lista = [1, 2, 3, 4, 5]
multiplicada = []
for i in lista:
    multiplicada.append(i * 3)

multiplicada = [i * 3 for i in lista]
multiPar = [i * 3 for i in lista if i % 2 == 0]
multidict = {i: i * 3 for i in lista}

mapMultiplica = map(lambda i: i * 3, lista)
mapMultPar = map(lambda i: i * 3, filter(lambda i: i % 2 ==0, lista))


#%% matriz 10 x 10 zerada
matriz = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

matriz = [[0 for j in range(10)] for i in range(10)]

# for linha in matriz: print(linha)

