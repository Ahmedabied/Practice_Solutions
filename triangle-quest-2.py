from functools import reduce
for i in range(1,int(input())+1):print(reduce((lambda a, v: a * 10 + v), map(lambda x: -1 * abs(x - i) + i, range(1, 2 * i)), 0))