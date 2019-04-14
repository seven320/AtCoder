# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える


a,b,c = map(int,input().split())

if (a==b and b==c):
    print("Yes")

else:
    print("No")
