# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7


W,a,b = map(int,input().split())

ans = min(abs(b-a-W),abs(b+W-a))
if a <= b and b-a <= W or b<=a and a-b <=W:
    ans = 0

print(ans)
