# encoding:utf-8

import copy
import numpy as np
import random

k,a,b = map(int,input().split())

cookie = 1

if b-a < 2:
    cookie += k

else:
    k -= (a-cookie)
    cookie = a

    cookie += (k//2)*(b-a)

    if k % 2 == 1:
        cookie += 1
    else:
        pass

print(cookie)
