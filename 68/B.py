# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math


N = int(input())

ans = 1
cnt_ans = 0
for i in range(1,N+1):
    tmp = i
    cnt = 0
    while tmp % 2 == 0:
        tmp //= 2
        cnt += 1
    if cnt > cnt_ans:
        ans = i
        cnt_ans = cnt

print(ans)
