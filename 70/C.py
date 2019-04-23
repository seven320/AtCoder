# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

N = int(input())
T = [int(input()) for i in range(N)]


def lcm(a,b):
    return (a * b) // fractions.gcd(a,b)

ans = 1
for t in T:
    ans = lcm(ans,t)

print(ans)
