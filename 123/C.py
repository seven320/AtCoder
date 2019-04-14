# encoding:utf-8
import copy
import numpy as np
import random
import math
import bisect #bisect_left　これで二部探索の大小検索が行える

n = int(input())
traffic_time = []
for i in range(5):
    traffic_time.append(int(input()))

traffic_time.sort()

wait_time = math.ceil(n/traffic_time[0])
# print(wait_time)
# if wait_time <= 1:
#     wait_time = 0
wait_time -= 1
# if n%traffic_time[0] == 0:
#     wait_time -= 1

wait_time = max(wait_time,0)

print(wait_time+5)
