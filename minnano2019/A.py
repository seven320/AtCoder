# encoding:utf-8

import copy
import numpy as np
import random


n,k = map(int,input().split())

if 2*k <= n+1:
    answer = "YES"
else:
    answer = "NO"

print(answer)
