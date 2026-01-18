l = []
for i in range(10):
    x = int(input("Type a number: "))
    l.append(x)
sum = 0
for i in range(10):
    sum = sum + l[i]
print("Summa:", sum)

a = True
for i in range(9):
    if(l[i] > l[i+1]):
        a = False
print("In rising order:", a)