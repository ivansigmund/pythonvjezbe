# napišite program koji upiše 2 vektora i izračuna kosinus kuta između ta dva vektora

import math

N = int(input())

a = []
b = []

for i in range(N):
    a.append(float(input()))
    b.append(float(input()))
    
sqa2 = (i*i for i in a)
sqb2 = (i*i for i in b)
ab = (i*j for i,j in zip(a,b))

ab = sum(ab)
sqa2 = math.sqrt(sum(sqa2))
sqb2 = math.sqrt(sum(sqb2))

print("cos(theta) je  ", ab/sqa2/sqb2)

