# encoding:utf-8
import copy
import numpy as np
import random

H,W = map(int,input().split())
h,w = map(int,input().split())


ans = H*W
ans -= (h*W+H*w)
ans += h*w

print(ans)
