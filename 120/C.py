# encoding:utf-8
import copy
import numpy as np
import random
# import pandas as pd
# import torch


s = list(str(input()))


count = [0,0]
for i in range(len(s)):
    count[int(s[i])] += 1

ans = 2*min(count[0],count[1])
#
print(ans)
# escape = False
# begin = len(s)
#
# def rem(s):
#     for i in range(1,len(s)):
#         # print(s)
#         if s[i-1] != s[i]:
#             s.pop(i)
#             s.pop(i-1)
#             break
#     return s
#
#
# pre = len(s)
# proceed = 0
# while proceed != pre:
#     pre = len(s)
#     s = rem(s)
#     after = len(s)
#
# end = len(s)
# print(begin-end)
