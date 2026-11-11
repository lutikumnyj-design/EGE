from math import *

for N in range(1,10000):
    i = ceil(log2(N))
    L = 248
    I = ceil(L * i / 8)
    if I * 75600 > 16 * 2**20:
        print(N)
        break