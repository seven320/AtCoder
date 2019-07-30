# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

S = [0,0,0]
for i in range(3):
    S[i] = str(input())

a,b,c = 0,0,0
next = "a"

def check(a,b,c,next):
    if next == "a":

        try:
            next = S[0][a]
            a += 1
        except:
            return 0,0,0,0,"A"
    elif next == "b":

        try:
            next = S[1][b]
            b += 1
        except:
            return 0,0,0,0,"B"
    else:
        try:
            next = S[2][c]
            c += 1
        except:
            return 0,0,0,0,"C"
    return a,b,c,next,0

while True:
    a,b,c,next,ans = check(a,b,c,next)
    if ans != 0:
        break
print(ans)
