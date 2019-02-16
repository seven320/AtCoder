# encoding:utf-8
import copy
import numpy as np
import random

n = int(input())
a = [int(i) for i in input().split()]

def fight(a):
    a.sort()
    survive = [a[0]]
    for i in range(1,len(a)):
        if a[i]%a[0]!=0:
            survive.append(a[i]%a[0])
    return survive

while len(a)>1:
    a = fight(a)

print(a[0])
