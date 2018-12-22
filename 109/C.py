#encoding utf-8

import math
from functools import reduce

#複数の最大コゥ約数
def gcd(a,b):
    l = max(a,b)
    m = min(a,b)
    while m != 0:
        extra = l%m
        l = m
        m = extra
    return l

def gcd_multi(numbers):
    return reduce(gcd,numbers)

n,X = map(int, input().split())

x = [int(i) for i in input().split()]

x.append(X)
x.sort()

minus=[]

for i in range(len(x)-1):
    minus.append(x[i+1]-x[i])


D = gcd_multi(minus)

print(int(D))
