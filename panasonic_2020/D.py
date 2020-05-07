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

def check_ans(nums):
    cnt = 0
    for num in nums:
        num = int(num)
        if num == cnt:
            cnt += 1
        elif num < cnt:
            pass
        else:
            return False
    return True

def make_anss(anss, n):
    new_anss = []
    ns = [str(i) for i in range(n + 1)]
    for ans in anss:
        for n in ns:
            p_anss = ans + n
            if check_ans(p_anss):
                new_anss.append(p_anss)
    return new_anss

anss = ["0"]
for i in range(N - 1):
    anss = make_anss(anss, i + 1)
dics = {
    "0": "a",
    "1": "b",
    "2": "c",
    "3":"d",
    "4":"e",
    "5":"f",
    "6":"g",
    "7":"h",
    "8":"i",
    "9":"j"
    }
for ans in anss:
    print(ans.translate(str.maketrans(dics)))




    