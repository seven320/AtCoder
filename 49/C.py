# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

S = str(input())
S = list(S)
S.reverse()
S = "".join(S)

def check(T):
    if len(S) == 0:
        return 1
    adds = ["maerd","remaerd","esare","resare"]
    q = copy.deepcopy(adds)
    while len(q) > 0:
        t = q.pop()
        if t == S:
            return 1
        for add in adds:
            if S[len(t):len(t+add)] == add:
                q.append(t+add)
    return 0

if check(""):
    print("YES")
else:
    print("NO")
