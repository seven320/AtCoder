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

N = int(input())
s = [0 for i in range(N)]
for i in range(N):
    s[i] = list(str(input()))
# print(s)

for i in range(N):
    s[i].sort()
    s[i] = "".join(s[i])
# print(s)

dic = {}
for i in range(N):
    if s[i] in dic.keys():
        dic[s[i]] += 1
    else:
        dic[s[i]] = 1

ans = 0
for key in dic.keys():
    if dic[key] > 1:
        ans += dic[key]*(dic[key] - 1)//2

print(ans)
