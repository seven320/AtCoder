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

k,x = LI()



ans = [x-k+1+i for i in range(2*k-1)]
for i in range(len(ans)):
    print(ans[i],end=" ")

print("")
