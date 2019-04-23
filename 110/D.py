# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import itertools


N,M = map(int,input().split())
primes = {}
# primes[1] = 1
tmp = 2
while M != 1:
    if M%tmp==0:
        M //= tmp
        if tmp in primes.keys():
            primes[tmp] += 1
        else:
            primes[tmp] = 1
    else:
        tmp += 1

def combination(n,r,rtn):
    if r > 0 and n > 0:
        for i in range(r):
            rtn += combination(n-1,r-i,rtn)
    else:
        return 1



# print(primes)
ans = 1
for key in primes.keys():
    ans *= combination(N,primes[key])
    if ans > (10**9+7):
        ans = ans % (10**9+7)

print(ans)
