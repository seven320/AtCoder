# encoding:utf-8
import copy
import numpy as np
import random

nums = list(input())
nums = [int(i) for i in nums]

def make2digits(n):
    digits = []
    for i in range(3):
        if n % 2 == 1:
            digits.append(1)
        else:
            digits.append(0)
        n = n//2
    return digits

for i in range(8):
    count = nums[0]
    choices = make2digits(i)
    # print(choices)
    for j in range(len(choices)):
        if choices[j]==0:
            count -= nums[j+1]
        else:
            count += nums[j+1]
    # print(count)
    if count == 7:
        ans_choice = choices
        break


plusminus = ["-","+"]
ans = ""
nums = [str(i) for i in nums]
for i in range(3):
    ans = ans + nums[i] + plusminus[ans_choice[i]]

ans = ans+nums[-1]+"=7"
print(ans)
