import math

def questao05_3():
    t = (22, 33, 77, 55, 66, 11, 99)
    e = 33

    def funcao(tt, ee):
        if ee in tt:
            pos = tt.index(ee)
            nova_tupla = tt[:pos] + tt[pos+1:]
            return nova_tupla

        return tt


def questao09():
    a = 100
    b = 100
    c = 120

    X = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    A = math.degrees(math.acos(X))

    Y = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
    B = math.degrees(math.acos(Y))

    Z = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    C = math.degrees(math.acos(Z))

    import turtle
    # a + B + c + A + b
    turtle.left(360)
    turtle.speed('slowest')

    turtle.forward(a)
    turtle.left(180 - B)

    turtle.forward(c)
    turtle.left(180 - A)

    turtle.forward(b)
    turtle.Screen().exitonclick()

#questao09()


def questao18():
    import turtle

    haste = 60
    lados = 5
    angulo = 360 / lados

    # turtle.speed('slowest')
    turtle.left(360)

    for l in range(lados):
        turtle.forward(haste)
        turtle.back(haste)
        turtle.left(angulo)

    interno = (lados - 2) * 180
    externo = (180 - angulo) / 2

    #ir para fora
    turtle.forward(haste)
    turtle.left(180 - angulo)
    for l in range(lados):
        turtle.forward(haste)
        turtle.left(angulo)

    turtle.Screen().exitonclick()

questao18()
