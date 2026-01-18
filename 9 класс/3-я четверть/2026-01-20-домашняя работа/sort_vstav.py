l = [3,4,2,3,67,21,8]

for i in range(1, len(l)):
    a = l[i]
    for j in range(i-1, -1, -1):
        if(l[j] >= a):
            l[j+1] = l[j]
            l[j] = a

for i in l:
    print(i)