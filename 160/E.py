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

X, Y, A, B, C = LI()
p = LI()
q = LI()
r = LI()

p.sort(reverse= 1)
q.sort(reverse= 1)
r.sort(reverse= 1)

def solve():
    ans = 0
    p_selected = p[:X]
    q_selected = q[:Y]
    p_selected.sort()
    q_selected.sort()
    p_cnt = 0
    q_cnt = 0
    r_selected = r[:min((X + Y), len(r))]
    # print(p_selected, q_selected)

    ans += sum(p_selected) + sum(q_selected)
    for r_i in r_selected:
    
        if q_cnt < Y and p_cnt < X:
            if p_selected[p_cnt] >= q_selected[q_cnt]:
                if q_selected[q_cnt] < r_i:
                    ans += r_i - q_selected[q_cnt]
                    q_cnt += 1
                else:
                    return ans
            elif p_selected[p_cnt] < q_selected[q_cnt]:
                if p_selected[p_cnt] < r_i:
                    ans += r_i - p_selected[p_cnt]
                    p_cnt += 1
                else:
                    return ans
        elif q_cnt < Y and p_cnt >= X:
            if q_selected[q_cnt] < r_i:
                ans += r_i - q_selected[q_cnt]
                q_cnt += 1
            else:
                return ans
        elif p_cnt < X and q_cnt >= Y:
            if p_selected[p_cnt] < r_i:
                ans += r_i - p_selected[p_cnt]
                p_cnt += 1
            else:
                return ans

    return ans

ans = solve()

print(ans)