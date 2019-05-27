# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import numpy as np

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000
n = int(input())
d = {}
for i in range(n):
     s,p=input().split()
     try:
          d[s][int(p)]=i+1
     except:
          d[s]={int(p):i+1}
k=sorted(d.keys())
print(d)
# for x in k:
#      d_=d[x]
#      k_=sorted(d_.keys())[::-1]
#      for y in k_:
#           print(d_[y])
