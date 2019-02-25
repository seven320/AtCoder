# encoding:utf-8
import copy
import numpy as np
import random

n = int(input())
h = [int(i) for i in input().split()]

count = 0

stack = []
stack.append(h)
while len(stack) != 0:
    group = stack.pop()
    # print(group)

    count += min(group)
    minus = min(group)
    for i in range(len(group)):
        group[i] -= minus

    begin = 0
    # print(group)
    for i in range(len(group)):
        if group[i] == 0:
            if len(group[begin:i])!=0:
                stack.append(group[begin:i])
            begin = i+1
        elif i == len(group)-1:
            if len(group[begin:])!=0:
                stack.append(group[begin:])
    # print(stack)
    # print(count)
print(count)
