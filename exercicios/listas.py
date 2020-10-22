def rodar(func):
    if __name__ == '__main__':
        print('-' * 10,func.__name__, '-' * 10)
        func()

def questao04():
    """
    Faça um Programa que leia um vetor de 10 caracteres,
    e diga quantas consoantes foram lidas. Imprima as consoantes.
    """
    palavra = input('palavra: ')
    qtd = 0
    for letra in palavra:
        if letra not in 'aeiou':
            print('consoantes: ', letra)
            qtd += 1
    print('numero de consoantes', qtd)

def questao06():
    """
    Faça um Programa que peça as quatro notas de 10 alunos,
    calcule e armazene num vetor a média de cada aluno,
    imprima o número de alunos com média maior ou igual a 7.0.
    """
    import random
    alunos = []

    # entrada de dados
    for i in range(10):
        notas_entrada = []
        for j in range(4):
            notas_entrada.append(random.randint(5, 10))
        alunos.append(notas_entrada)

    # calculo da média de CADA ALUNO
    qtd = 0
    for notas in alunos:
        media = sum(notas) / len(notas)
        if media >= 7:
            qtd += 1

    print(qtd)

def questao07():
    """
    Faça um Programa que leia um vetor de 5 números inteiros,
    mostre a soma, a multiplicação e os números.
    """
    import random
    valores = [random.randint(1, 10) for i in range(5)]

    ##### forma alternativa
    # valores = []
    # for i in range(5):
    #     valores.append(random.randint(1, 10))

    soma = 0
    multiplicacao = 1
    for i in valores:
        soma += i
        multiplicacao *= i

    print('soma -> ', soma)
    print('multiplicacao -> ', multiplicacao)
    print('numeros -> ', ', '.join([str(i) for i in valores]))
    print('numeros (errada) -> ', valores)


    # reduce
    import operator
    from functools import reduce
    ### jeito senior
    reduce(operator.mul, valores, 1)

    ### metido a besta
    reduce(lambda x, y: x * y, valores, 1)

    ### simplao
    def mult(x, y):
        return x * y
    reduce(mult, valores, 1)

def questao08():
    """
    Faça um Programa que peça a idade e a altura de 5 pessoas,
    armazene cada informação no seu respectivo vetor.
    Imprima a idade e a altura na ordem inversa a ordem lida.
    :return:
    """
    import random
    idade = [random.randint(21, 49) for i in range(5)]
    altura = [random.randint(149, 180) for i in range(5)]

    for pos, idade in enumerate(idade):
        print(f'{idade} <-> {altura[pos]}')

        ##### jeitos antigos de formatar uma string
        # print('%s <-> %s' % idade, altura[pos])
        # print(idade, '<-> %s', altura[pos])

    ##### senior (errado de acordo com o enunciado)
    # lista = [(random.randint(21, 49), random.randint(21, 49)) for i in range(5)]
    # lista_reversa = lista[::-1]

def questao09():
    """
    Faça um Programa que leia um vetor A com 10 números inteiros,
    calcule e mostre a soma dos quadrados dos elementos do vetor.
    """
    import random
    print(sum([random.randint(1, 10) ** 2 for i in range(10)]))

    # explicito
    # somatorio = 0
    # for i in range(10):
    #     valor = random.randint(1, 10)
    #     quadrado = valor ** 2
    #     somatorio += quadrado
    #
    # print(somatorio)

def questao10():
    """
    Faça um Programa que leia dois vetores com 10 elementos cada.
    Gere um terceiro vetor de 20 elementos,
    cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
    c = (1, 2, 3, 4, 5)
    d = (6, 7, 8, 9, 0)
    i = (1, 6, 2, 7, 3, 8, 4, 9, 5, 0)
    """
    import random
    c = [random.randint(1, 10) for i in range(10)]
    d = [random.randint(1, 10) for i in range(10)]

    r = []
    for pos, el in enumerate(c):  # jeito iniciante:   for pos in range(len(c))
        r.append(el)
        r.append(d[pos])

    # exemplo para ninguem tentar em casa sem supervisão de um adulto
    r2 = [item for sublist in [(el, d[pos]) for pos, el in enumerate(c)] for item in sublist]
    print(r)


@rodar
def questao12():
    """
    Foram anotadas as idades e alturas de 30 alunos.
    Faça um Programa que determine quantos alunos com
    mais de 13 anos possuem altura inferior à média de altura desses alunos.
    """
    import random
    n = 30
    idades = [  random.randint(8, 18) for i in range(n)]
    alturas = [random.randint(120, 190) for i in range(n)]
    contagem = 0
    media = sum(alturas) / len(alturas)
    for i in range(n):
        if idades[i] > 13 and alturas[i] < media:
            contagem += 1
    print(contagem)

    #### jeito doido de fazer
    qtd = len([pos for pos, idade in enumerate(idades) if idade > 13 and alturas[pos] < media])
