# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える

length = []

for i in range(5):
    length.append(int(input()))

k = int(input())

length.sort()
if length[-1]-length[0] > k:
    print(":(")
else:
    print("Yay!")
