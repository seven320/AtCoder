# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math

N = int(input())
S = str(input())


cnt = S.count(".")

l = [cnt] #all black
for i in range(N):
    if S[i]==".":
        cnt -= 1
        l.append(cnt)
    else:
        cnt += 1
        l.append(cnt)

# print(l)
print(min(l))
