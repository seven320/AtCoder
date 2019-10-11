# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))


"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


A,B = LI()

gcd = fractions.gcd(A,B)
ans = 1
for facter in factorization(gcd):
    if facter[0] == 1:
        pass
    else:
        ans += 1
print(ans)


'''
12 18
1 2 3 6
1 2 3

6 9
1 3
1 2 3

420 660
210 330
105 165
35 55
7 11

2**2*3
1 2 3 5
'''
