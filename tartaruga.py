import turtle

turtle.shape('turtle')
turtle.speed('slowest')

turtle.left(360)

linhas = int(360 / 15)

for x in range(linhas):
    turtle.forward(100)
    turtle.write(f'{x * 15}°')
    turtle.back(100)
    turtle.left(15)

turtle.delay(100)

