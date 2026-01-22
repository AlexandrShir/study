from string import *

str = "shirokovs060@gmail.com"

a = str.find("@")

domen = str[a+1:]
print(domen)