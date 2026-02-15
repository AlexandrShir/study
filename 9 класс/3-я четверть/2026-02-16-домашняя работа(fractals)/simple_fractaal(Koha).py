import turtle as t
from string import *

a = "FLFRRFLF"
n = 4

str = "FLFRRFLF"
t.teleport(-500, 300)
t.speed(50)

def parcerc(l, p):
    for i in l:
        if(i == 'F'):
            t.forward(30//p)
        if(i == 'L'):
            t.left(60)
        if(i == 'R'):
            t.right(60)

for i in range(0, n-1):
    str1 = ""
    for j in str:
        if(j == 'F'):
            str1 = str1 + a
        else:
            str1 = str1 + j
    str = str1

parcerc(str, n)            #повторение функций под углом 120 - для снежинки Коха - фрактал, где n - его глубина
t.right(120)
parcerc(str, n)
t.right(120)
parcerc(str, n)
t.done()