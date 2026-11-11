from math import *

for L in range(10000, 1, -1):
    N = 10 + 52 + 963
    i = ceil(log2(N))
    I = ceil(i*L/8)
    if I * 2000 < 693*2**10:
        print(L)
        break
