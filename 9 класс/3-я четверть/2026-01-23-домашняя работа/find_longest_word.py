from string import *
str = "Aboba upala naaaaa lapu aboba"

l = str.split()
max_size = 0
max_str = ""
for i in l:
    if(len(i) > max_size):
        max_size = len(i)
        max_str = i


print(max_str, max_size)        