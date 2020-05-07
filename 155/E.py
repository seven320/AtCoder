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



def solve(N):
    n_s = list(str(N))

    n_s = [0] + n_s
    n_s.reverse()

    def cnt_paper(s):
        tmp = 0
        # print(s)
        for s_i in s:
            tmp += int(s_i)
        return tmp

    anss = [0 for i in range(len(n_s) + 1)]
    for i in range(len(n_s)):
        if int(n_s[i]) == 5 and int(n_s[i + 1]) >= 5 or int(n_s[i]) >= 6:
            anss[i+1] += 1
        else:
            anss[i] += int(n_s[i])

    anss.reverse()
    # print(anss)
    ans = cnt_paper(anss)
    tmp = ""
    for i in range(len(anss)):
        tmp += str(anss[i])

    # print(tmp)
    # print(anss)
    print(int(tmp))
    print(cnt_paper(list(str(int(tmp) - N))))
    ans += cnt_paper(list(str(int(tmp) - N)))
    return min(ans, cnt_paper(list(str(N))))

N = int(input())
print(solve(N))

