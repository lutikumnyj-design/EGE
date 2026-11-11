from math import log2, ceil, floor

L = 101
n = 10 + 4090
N = 2048
i = ceil(log2(n))

I = ceil(L * i / 8)
V = I * N / 1024
print(V)
