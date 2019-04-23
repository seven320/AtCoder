# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math

N = str(input())


if N[0] == N[2]:
    print("Yes")
else:
    print("No")
