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

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

a = str(input())
b = str(input())
c = str(input())

all =[
    [a,b,c],
    [a,c,b],
    [b,a,c],
    [b,c,a],
    [c,a,b],
    [c,b,a]
]

def check_dig(str_a, str_b):
    double_nums = 0
    for i in range(1,min(len(str_a), len(str_b)) +1):
        part_a = str_a[-i:]
        part_b = str_b[:i]
        for j in range(len(part_a)):
            if part_a[j] == "?" or part_b[j] == "?" or part_b[j] == part_a[j]:
                pass
            else:
                break
        else:
            double_nums = len(part_a)
    # print(str_a, str_b)
    # print(double_nums)
    str_s = str_a
    for i in range(double_nums):

    return double_nums

ans = len(a) + len(b) + len(c)
cnt = -1
for orders in all:
    tmp = 0
    for i in range(2):
        tmp += check_dig(orders[i], orders[i + 1])
    cnt = max(cnt, tmp)

ans -= cnt
print(ans)

    