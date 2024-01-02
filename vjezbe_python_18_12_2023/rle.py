# kompresija

import sys
import itertools

def rle(src, dest):
    s = src.read()
    s = "".join( ["{}{}".format(len(list(v)), k) for k,v in itertools.groupby(s)])
    dest.write(s)
    
with open(sys.argv[1], "r") as src:
     with open(sys.argv[2], "w") as dest:
          rle(src, dest)
