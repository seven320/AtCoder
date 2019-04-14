# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math


a,b = map(int,input().split())

ans = 0
if a > b:
    ans += a
    a -= 1

else:
    ans += b
    b -= 1

ans += max(a,b)
print(ans)
