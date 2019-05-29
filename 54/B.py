# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
# import numpy as np

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N,M = map(int,input().split())
A = [0 for i in range(N)]
B = [0 for i in range(M)]
for i in range(N):
    A[i] = input()
for i in range(M):
    B[i] = input()

ans = False
for y in range(N-M+1):
    for x in range(N-M+1):
        for i in range(M):
            for j in range(M):
                if A[x+i][y+j] == B[i][j]:
                    pass
                else:
                    break
            else:
                continue
            break
        else:
            ans = True

if ans:
    print("Yes")
else:
    print("No")
