from turtle import *

screensize(3000, 3000)
tracer(False)
k = 10

left(90)
for i in range(6):
    forward(33*k)
    right(90)
    forward(20*k)
    right(90)
up()
forward(3*k)
right(90)
forward(9*k)
left(90)
down()
for i in range(6):
    forward(24*k)
    right(90)
    forward(25*k)
    right(90)

up()

for x in range(10, 20):
    for y in range(4, 27):
        goto(x*k, y*k)
        dot(3, 'red')

print((27-4)*(20-10))

update()
done()