# encoding:utf-8

import copy
import numpy as np
import random

a,b = map(int, input().split())

round = lambda x:(x*2+1)//2

print("{0:.0f}".format(round((a+b)/2)))
