# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000


N = int(input())
s = str(input())
s = list(s)

def step(first,second,rep):
    ls = [first,second]
    if ls == [0,0]:
        if rep == "o":
            third = 0
        else:
            third = 1
    elif ls == [0,1]:
        if rep == "o":
            third = 1
        else:
            third = 0
    elif ls == [1,0]:
        if rep == "o":
            third = 1
        else:
            third = 0
    else:
        if rep == "o":
            third = 0
        else:
            third = 1
    return second,third

def check(animals):
    first,second = step(animals[-1],animals[0],s[0])
    if second == animals[1]:
        return True
    else:
        return False

primes = [[0,0],[0,1],[1,0],[1,1]]
for first,second in primes:
    animals = [first]
    for i in range(N-1):
        animals += [second]
        rep = s[i+1]
        first,second = step(first,second,rep)
    print(animals)
    if check(animals):
        ans = ["S" if i == 0 else "W" for i in animals]
        ans = "".join(ans)
        print(ans)
        exit()

print(-1)
