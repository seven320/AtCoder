# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math

N = str(input())

if N[0]=="9" or N[1]=="9":
    print("Yes")

else:
    print("No")
