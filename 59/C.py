# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

n = int(input())
a = [int(i) for i in input().split()]

def solve(a):
    if a[0] > 0:
        status_pos = True
    elif a[0] < 0:
        status_pos = False

    tmp = 0
    ans = 0
    for i in range(n):
        tmp += a[i]
        if tmp == 0:
            ans += 1
            if status_pos:
                tmp = -1
            else:
                tmp = 1

        elif status_pos and tmp < 0:
            ans += 1+abs(tmp)
            tmp = 1
        elif status_pos == False and tmp > 0:
            ans += 1+abs(tmp)
            tmp = -1
        status_pos = not(status_pos)
    return ans

#初期が０の場合どっちも試してみる
if a[0] == 0:
    a[0] = 1
    ans = 1
    ans += solve(a)

    a[0] = -1
    ans2 = 1
    ans2 += solve(a)
    ans = min(ans,ans2)
#どっちも試す
else:
    ans = solve(a)
    #値反転
    ans3 = abs(a[0])+1
    if a[0] > 0:
        a[0] = -1
    else:
        a[0] = 1
    ans3 += solve(a)
    ans = min(ans,ans3)

print(ans)
