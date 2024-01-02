# dekompresija

import sys
import itertools

def unrle(src, dest):
    s = src.read()
    assert len(s)%2 == 0 #ocekujemo parni broj znakova u komprimiranoj datoteci
    
    ponavljanja = s[::2] #string znamenki od nultog do zadnjeg elementa po koraku 2
    ponavljanja = map(int, ponavljanja) #iterator koji vraca brojeve ponavljanja svakog znaka i pretvaramo ih u int
    
    znakovi = s[1::2] #string znakova krecemo od 1 do kraja po koraku 2
    
    s = [z*p for z,p in zip(znakovi, ponavljanja)] # radimo listu znak puta ponavljanje
    s = "".join(s) # spojimo sve elemente liste u jedan string
    dest.write(s)
    
with open(sys.argv[1], "r") as src:
     with open(sys.argv[2], "w") as dest:
          unrle(src, dest)
