from math import *

for L in range(1, 10000):
    N = 10 + 70
    i = ceil(log2(N))
    I = ceil(L*i/8)
    if 1234567*I > 24 * 2**20:
        print(L)
        break