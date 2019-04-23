# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math


S = str(input())

# print(S)
all = list("abcdefghijklmnopqrstuvwxyz")
all.sort()
for i in range(len(S)):
    if S[i] in all:
        all.remove(S[i])

if len(all) > 0:
    print(all[0])
else:
    print("None")
