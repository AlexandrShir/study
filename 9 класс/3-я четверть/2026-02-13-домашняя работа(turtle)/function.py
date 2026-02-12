import turtle as t

screen = t.Screen()
screen.screensize(400, 300)
def f(x):
    return 1.5*x + 40

t.forward(400)
t.backward(800)
t.forward(400)
t.left(90)
t.forward(300)
t.backward(600)
t.right(90)
t.teleport(0, 0)
def draw_func(f, step):
    a = 0
    t.teleport(a, f(a))
    while(a < 400-step):
        a = a + step
        t.goto(a, f(a))
    t.teleport(0, f(0))
    a = 0
    while(a > -400+step):
        a = a - step
        t.goto(a, f(a))
draw_func(f, 50)
t.done()