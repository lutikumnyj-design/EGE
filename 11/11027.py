from math import *

for L in range(10000, 1, -1):
    N = 52 + 458 + 10
    i = ceil(log2(N))
    I = ceil(i*L/8)
    if I * 862 < 276 * 2**10:
        print(L)
        break