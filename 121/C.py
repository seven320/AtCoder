# encoding:utf-8
import copy
import numpy as np
import random

n,m = map(int,input().split())

shops = []
for i in range(n):
    a,b = map(int,input().split())
    shops.append([a,b])


# i　何軒めの店まで見ているか，何本買うか
# dp[i][j]

# dp = [[10**10 for i in range(m)] for j in range(n)]

shops.sort()
ans = 0
count = m
# print(shops)
i = 0
while True:
    # print(count,ans)
    yen,num = shops[i]
    if count-num > 0:
        count -= num
        ans += yen*num
        # print(ans)
        i += 1
    else:
        ans += yen*count
        # print(ans)
        count -= count
        break


print(ans)
