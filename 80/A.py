# encoding:utf-8
import copy
import numpy as np
import random

n,a,b = map(int, input().split())


ans = min(b,a*n)

print(ans)
