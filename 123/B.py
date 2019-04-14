# encoding:utf-8
import copy
import numpy as np
import random
import bisect #
import math

ans = 0
menu_time = []
for i in range(5):
    menu_time.append(int(input()))

amari = 10
for i in range(5):
    if menu_time[i]%10>0:
        amari = min(menu_time[i]%10,amari)
    ans += math.ceil(menu_time[i]/10)*10

ans -= 10
ans += amari


print(ans)
