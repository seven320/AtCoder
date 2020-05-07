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

N = int(input())
A = LI()

ball_dic = {}
for i in range(N):
    if A[i] in ball_dic.keys():
        ball_dic[A[i]] += 1
    else:
        ball_dic[A[i]] = 1

def cnt_ans(ball_sets):
    cnt = 0
    for ball_set in ball_sets:
        if ball_set > 1:
            cnt += ball_set * (ball_set - 1) // 2
    return cnt
    
basic_ans = cnt_ans(ball_dic.values())

for i in range(N):
    n = ball_dic[A[i]]
    if n > 1:
        ans = basic_ans - (ball_dic[A[i]] - 1)
    else:
        ans = basic_ans
    print(ans)

    
        
