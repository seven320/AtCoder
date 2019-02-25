# encoding:utf-8
import copy
import numpy as np
import random

l = [int(i) for i in input().split()]
l.sort()
print(l[1]*l[0]//2)
