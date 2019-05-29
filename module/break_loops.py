# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000


for i in range(10):
    for j in range(3):
        print(i)
        if i == 3:
            break
    else: # もし上の部分でbreakがなければelse文が動くのでbreakをcontinueでスキップできる
        continue
    break

    
