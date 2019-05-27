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
ab = [[] for i in range(N)]
for i in range(N):
    ab[i] = [int(i) for i in input().split()]

def battle(player1,player2):
    hp1,at1 = player1
    hp2,at2 = player2
    # while hp1 > 0 and hp2 > 0:
    #     hp1 -= at2
    #     hp2 -= at1
    num_at1 = hp1 / at2
    num_at2 = hp2 / at1
    if math.ceil(num_at1) == math.ceil(num_at2):
        return -1
    if num_at1 < num_at2:
        return 1
    else:
        return 0

#1roop
ans_ab = ab[0]
num_ans = 0
for i in range(1,N):
    # print(num_ans,i)
    # print(ans_ab,ab[i])
    a = battle(ans_ab,ab[i])
    # print(a)
    if a == -1:
        break
    if a == 1:
        ans_ab = ab[i]
        num_ans = i
    else:
        pass

if a == -1:
    pass
else:
    for i in range(num_ans):
        a = battle(ans_ab,ab[i])
        if a == -1 or a == 1:
            a = -1
            break

if a == -1:
    print(-1)
else:
    print(num_ans+1)
