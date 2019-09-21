# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect
from collections import deque

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
B = [[] for i in range(N)]
for i in range(N):
    B[i] = LI()
    for j in range(N-1):
        B[i][j] -= 1

A = copy.deepcopy(B)
for i in range(N):
    A[i].reverse()

match = 1
ans = 1
answer_choice = []
while match:
    match = 0
    status = [i for i in range(N)]
    for now in status:
        if len(A[now]) == 0:
            pass
        else:
            enemy = A[now][0]
            if A[enemy][0] == now:
                answer_choice.append((enemy, now))
                A[enemy].pop(0)
                A[now].pop(0)
                match = 1
                try:
                    status.remove(enemy)
                except:
                    pass

if len(answer_choice) != (N-1)*N//2:
    print(-1)
    exit()

answer_choice.reverse()
tmp = []
for choice_i in answer_choice:
    i,j = choice_i
    if i in tmp or j in tmp:
        ans += 1
        tmp = [i,j]
        # continue
    else:
        tmp.append(i)
        tmp.append(j)

print(ans)
