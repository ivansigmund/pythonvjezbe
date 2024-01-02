# napište program koji ispisuje tablicu množenja



L = [ x*0.1 for x in range(31,41)]

L2 = [ ["{:5.2f}".format(i*j) for j in L] for i in L] # lista listi

print(L2[0])
print("...")
print(L2[-1]) #ispisuje posljednji element (podlistu)
print()
print()

#Ispisuje cijelu tablicu s okomitim crtama i bez uglatih zagrada
L2 = ["|".join(["{:5.2f}".format(i*j) for j in L]) for i in L] # lista stringova, svaki sadrži redak

print(L2[0])
print(L2[1])
print("...")
print(L2[-1])
print()
print()

print("Tablica množenja b1:")
print("\n".join(L2))  # svi reci spoje u jedan string odvojen znakom za novu liniju
