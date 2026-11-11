data = '134534534'

summ = 0
for i in set(data):
    summ += data.count(i) * int(i)
print(summ)