# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math


N,K = map(int,input().split())
l = [int(i) for i in input().split()]


l.sort(reverse=True)

print(sum(l[:K]))
