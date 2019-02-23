# encoding:utf-8
import copy
import numpy as np
import random

x,y = map(int,input().split())

count_2 = 0

multi = y//x
by_2 = 1
count = 0
while multi >= by_2:
    by_2 *=2
    count += 1

print(count)
