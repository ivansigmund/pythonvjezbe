import math

N = int(input())

L = range( 0, N+1)
L = (x*math.pi/N for x in L)

L = map(math.sin, L)

print(sum(L))
