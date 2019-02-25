# encoding:utf-8
import copy
import numpy as np
import random
import queue

n = int(input())

withdraws = [1]
price = 1
while True:
    price *= 6
    if price <= 10**5 and price <= n:
        withdraws.append(price)
    else:
        break

price = 1
while True:
    price *= 9
    if price <= 10**5 and price <= n:
        withdraws.append(price)
    else:
        break


withdraws.sort()
# print(withdraws)
money = 0
count = 0


# 幅優先探索
'''
que = queue.Queue()

que.put((0,0))
memory = []
while not(que.empty()):
    money,count = que.get()
    print(money,count)
    if money > n:
        pass
    else:
        for withdraw in withdraws:
            if money+withdraw == n:
                print(count+1)
                exit()

            elif money+withdraw in memory:
                pass
            else:
                memory.append(money+withdraw)
                next = (money+withdraw,count+1)
                que.put(next)
'''
'''
# 分割

ans = 10**10
if n < 6:
    ans = n
for i in range(n+1):
    t = i
    count = 0
    while t>0:
        count += t%6
        t = t//6
    t = n - i
    while t>0:
        count += t%9
        t = t//9
    # print(ans)
    ans =min(ans,count)

print(ans)

'''

max_num = 10**5
dp = [99999999]*(n+1)
dp[0] = 0
for i in range(1,n+1):
    # print(dp)
    dp[i] = dp[i-1]+1
    k = 6
    while i>=k:
        dp[i] = min(dp[i],dp[i-k]+1)
        k *= 6
    k = 9
    while i>=k:
        dp[i] = min(dp[i],dp[i-k]+1)
        k *= 9



print(dp[n])
