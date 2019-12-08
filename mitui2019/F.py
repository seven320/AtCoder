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

T1, T2 = LI()
A1, A2 = LI()
B1, B2 = LI()


# print(T1 * A1 + T2 * A2)
# print(T1 * B1 + T2 * B2)

diff_dis = abs((T1 * A1 + T2 * A2) - (T1 * B1 + T2 * B2))
min_dis = min((T1 * A1 + T2 * A2),(T1 * B1 + T2 * B2))
if diff_dis == 0:
    print("infinity")
    sys.exit(0)

if A1 > B1 and A2 > B2 or A1 < B1 and A2 < B2:
    print(0)
    sys.exit(0)
set_cnt = math.ceil(min_dis / diff_dis)

ans = (max(A1, B1) - min(A1, B1)) * T1 // diff_dis * 2

print(ans -1)
