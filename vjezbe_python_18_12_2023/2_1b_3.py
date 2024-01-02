# napište program koji ispisuje tablicu množenja



L = [ x*0.1 for x in range(31,41)]
print()
print()
print()
print("Ispis s default separatorom (\" \"):")
print("Tablica množenja b1:")
for x in L:
     print(*["{:5.2f}".format(x*y) for y in L])
print()
print()
print()

print("Ispis sa separatorom \" | \":")
print("Tablica množenja b1:")
for x in L:
     print(*["{:5.2f}".format(x*y) for y in L], sep="|")
