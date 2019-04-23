# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math

x,a,b = map(int,input().split())


if abs(x-a) > abs(x-b):
    print("B")
else:
    print("A")
