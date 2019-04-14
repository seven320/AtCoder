# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math


N,K = map(int,input().split())
S = str(input())

now,cnt = 1,0
Nums = []
for i in range(N):
    if S[i] == str(now):
        cnt += 1
    else:
        Nums.append(cnt)
        cnt = 1
        now = 1 - now

if cnt!=0:
    Nums.append(cnt)

if len(Nums)%2==0:
    Nums.append(0)

#累積和
"""
Sums = [0]
tmp = 0
for i in range(len(Nums)):
    tmp += Nums[i]
    Sums.append(tmp)

ans = 0
Add = 2*K+1
for i in range(len(Sums)):
    if i%2==0:
        left = i
        right = min(i+Add,len(Sums)-1)
        tmp = Sums[right]-Sums[left]
        ans = max(tmp,ans)
"""
# 尺取り法
ans = 0
add = 2*K+1
left = 0
right = min(0+add,len(Nums))
pre = sum(Nums[left:right])
ans = pre
for i in range(len(Nums)-add):
    if i%2==0:
        left = i
        right = min(i+add,len(Nums)-1)
        pre += sum(Nums[right:right+2])-sum(Nums[left:left+2])
        ans = max(pre,ans)

print(ans)
