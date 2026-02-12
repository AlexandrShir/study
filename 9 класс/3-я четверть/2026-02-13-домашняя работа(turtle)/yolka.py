import turtle as t

d = 50 #расстояние  между ветками(фиксировано)
a0 = 50
d0 = 10  #a0 и d0 - первый элемент и разность геометрической прогрессии для размера веток

l = [a0]
def yolka(n):
    t.left(90)
    t.goto(0, d*(n//2))
    t.left(180)
    for i in range(0, n):
        t.right(70)
        t.forward(l[-1])
        t.left(180)
        t.forward(l[-1])
        t.right(40)
        t.forward(l[-1])
        t.left(180)
        t.forward(l[-1])
        t.left(110)
        t.forward(d)
        l.append(l[-1] + d0)
t.speed(5)
yolka(4)
t.done()