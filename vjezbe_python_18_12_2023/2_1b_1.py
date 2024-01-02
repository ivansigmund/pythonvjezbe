# napište program koji ispisuje tablicu množenja
import sys

L = [ x*0.1 for x in range(31,41)]

print("Tablica množenja 1b:")

for i in L:
    #nulti stupac ispisujemo zasebno
    # print("{:5.2f}".format(i*L[0]), end='')  #prvi način
    sys.stdout.write("{:5.2f}".format(i*L[0])) #drugi način
    
    #ostale stupce odvajamo znakom "|"
    for j in L[1:]:
        #print("|{:5.2f}".format(i*j), end='')
        sys.stdout.write(" | {:5.2f}".format(i*j)) #drugi način
    print()  #nova linija
