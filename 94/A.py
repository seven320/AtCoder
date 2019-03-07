# encoding:utf-8
import copy
import numpy as np
import random


a,b,x = map(int,input().split())

if a<= x <= a+b:
    ans = True
else:
    ans = False

if ans:
    print("YES")
else:
    print("NO")
