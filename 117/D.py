# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect
import numpy as np

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

N,K = LI()
A = LI()

cnt_digits = np.zeros(50)

def num2digit(num):
    digits = np.zeros(50)
    for i in range(50):
        if num <= 0:
            break
        else:
            digits[i] = num % 2
            num = num // 2
    return digits
for i in range(N):
    cnt_digits += num2digit(A[i])
cnt = 0
k = copy.deepcopy(K)
for i in range(50):
    if k <= 0:
        break
    else:
        cnt += 1
        k = k //2
ans = 0
# print(cnt_digits)
for k_i in reversed(range(50)):
    if k_i <= cnt:
        pass
        if cnt_digits[k_i] > N - cnt_digits[k_i]:
            ans += cnt_digits[k_i] * (2 ** k_i)
        else:
            ans += (N - cnt_digits[k_i]) * (2 ** k_i)
    else:
        ans += cnt_digits[k_i] * (2 ** k_i)
print(int(ans))
