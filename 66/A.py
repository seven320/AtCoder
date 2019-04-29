# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math


a,b,c = map(int,input().split())
ans = a+b+c
ans -= max(a,b,c)
print(ans)
