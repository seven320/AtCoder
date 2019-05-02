# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7


N,K = map(int,input().split())


#素因数分解
from collections import Counter

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
    # print(table_)
    return table_

dic = factorint(N)
cnt = 0
for key in dic.keys():
    cnt+=dic[key]

if K==1:
    print(N)
    exit()

if cnt >= K:
    ans = []
    keys = list(dic.keys())
    keys.sort()
    ans_cnt = 0
    for key in keys:
        for i in range(dic[key]):
            print(key,end=" ")
            ans_cnt += 1
            N //= int(key)
            if ans_cnt >= K-1:
                print(str(N))
                exit()

else:
    print("-1")
    exit()
