# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

S = str(input())
pos = S.find("WWBWBWW")

anss = ["Do", "Re", "Mi", "Fa", "So", "La", "Si"]
anss.reverse()
print(pos//2)
print(anss[pos//2])
