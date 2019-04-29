# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import itertools
from functools import reduce
from operator import mul
#素因数分解
from collections import Counter


N,M = map(int,input().split())
primes = {}
# primes[1] = 1
tmp = 2
max_count = 0
# while M != 1:
#     if M%tmp==0:
#         M //= tmp
#         if tmp in primes.keys():
#             primes[tmp] += 1
#             max_count = max(max_count,primes[tmp])
#         else:
#             primes[tmp] = 1
#     else:
#         tmp += 1


def factorint(N):
    table = []
    while(N > 1):
        for i in range(2,N+1):
            if N%i == 0:
                while N%i == 0:
                    N = N//i
                    table.append(i)
                break
    table_ = Counter(table)
    return table_

primes = factorint(M)


# def combination(n,r):
#     return math.factorial(n) // (math.factorial(n-r)*math.factorial(r))
def combination(n, r):
    """
    組み合わせの数 nCr
    :param n:
    :param r:
    :return:
    """
    r = min(n - r, r)
    if r == 0:
        return 1
    return reduce(mul, range(n, n - r, -1)) // reduce(mul, range(r, 0, -1))


# print(primes)
ans = 1
for key in primes.keys():
    tmp = combination(primes[key]+N-1,primes[key])

    ans = (ans*tmp)%(10**9+7)

print(ans)
