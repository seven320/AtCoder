# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000



#素因数分解
from collections import Counter



N = int(input())
table = []

def factorint(N):
    # table = []
    while(N > 1):
        for i in range(2,N+1):
            if N%i == 0:
                while N%i == 0:
                    N = N//i
                    table.append(i)
                break
    return table

for i in range(1,N+1):
    factorint(i)
table_ = Counter(table)

ans = 1
for key in table_.keys():
    ans = ans * (table_[key]+1) % mod

print(ans)
