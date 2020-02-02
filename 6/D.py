# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

c = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
for i in range(N):
    c.append(int(input()))

moved = []
left_num = 1
ans = 0
for i in range(N):
    if left_num == c[i]:
        left_num += 1
        for j in range(len(moved)):
            if moved[j] > left_num:
                moved = moved[j:]
                break
            elif moved[j] == left_num:
                left_num += 1
        moved.sort()
    else:
        moved.append(c[i])
        ans += 1

print(ans)


"""

4 3 1 2 5


2 4 3 1

"""