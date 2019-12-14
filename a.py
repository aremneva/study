import math
import random
s=input("Введите строку из 10 символов:")
n=list(s)
for i in range(10):
    if i%2==0:
        n[i]=i
    else:
        n[i]=random.choice(['a','b','c','d','e','f','g'])

s=str(n)
print(s)
