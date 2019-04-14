# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math

T = int(input())
anss = []
for i in range(T):
    size = int(input())
    way = str(input())
    ans = ""
    for j in range(len(way)):
        if way[j] == "E":
            ans += "S"
        else:
            ans += "E"
    anss.append(ans)
for i in range(T):
    print("Case #"+str(i+1)+": {0}".format(anss[i]))
