import math

N = int(input())

L = [math.sin(x*math.pi/N) for x in range(N+1)]

print(sum(L))
