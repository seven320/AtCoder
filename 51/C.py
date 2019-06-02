# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

sx,sy,gx,gy = map(int,input().split())

ans = []
# go
way1 = ["U"] * (gy-sy) + ["R"] * (gx-sx)
#return
way2 = ["D"] * (gy-sy) + ["L"] * (gx-sx)

way3 = ["L"] + ["U"] * (gy-sy+1) + ["R"] * (gx-sx+1) + ["D"]
way4 = ["R"] + ["D"] * (gy-sy+1) + ["L"] * (gx-sx+1) + ["U"]
ans += way1 + way2 + way3 + way4

print("".join(ans))
# print(len(ans))
