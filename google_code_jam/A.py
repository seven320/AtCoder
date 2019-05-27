cd
# encoding:utf-8
import copy
import numpy as np
import random
import math
import bisect #bisect_left　これで二部探索の大小検索が行える

T = int(input())
N = []
for i in range(T):
    N.append(int(input()))


ans = []
for i in range(T):
    ans_r = 1
    while ans_r < N[i]:
        check = True
        ans_l = N[i]-ans_r
        digit_r = len(str(ans_r))
        digit_l = len(str(ans_l))
        for digit in range(max(digit_l,digit_r)):
            if ((ans_r%(10**(digit+1))-(ans_r%(10**(digit))))//(10**digit))==4 or ((ans_l%(10**(digit+1))-(ans_l%(10**(digit))))//(10**digit))==4:
                check = False
                ans_r += 10**digit
                break

        if check:
            ans.append([ans_r,N[i]-ans_r])
            break


for i in range(T):
    print("Case #"+str(i+1)+": {0} {1}".format(ans[i][0],ans[i][1]))
