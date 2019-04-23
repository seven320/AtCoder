# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math

N = int(input())
a = [0 for i in range(N)]
for i in range(N):
    a[i] = int(input())
