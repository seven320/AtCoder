# encoding:utf-8

import copy
import numpy as np
import random

#n==100の時のコーナーケースに手間取った

d,n = map(int, input().split())
if n == 100:
    print(100**d*101)
    exit()
else:
    print(100**d*n)
