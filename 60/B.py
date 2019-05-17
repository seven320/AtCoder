# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

A,B,C = map(int,input().split())
extra = []

# import time
#
# now = time.time()
#
#
# mod = A
# while True:
#     mod += A
#     if mod % B == C:
#         print("YES")
#         break
#     if time.time()-now > 1:
#         print("NO")
#         break

for i in range(B):
    if i*A % B == C:
        print("YES")
        break

    if i == B-1:
        print("NO")
