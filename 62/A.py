# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

x,y = map(int,input().split())

group1 = [1,3,5,7,8,10,12]
group2 = [4,6,9,11]


ans = False
if x in group1 and y in group1:
    ans = True

elif x in group2 and y in group2:
    ans = True

if ans:
    print("Yes")
else:
    print("No")

    
