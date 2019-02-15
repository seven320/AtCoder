# encoding:utf-8

import copy
import numpy as np
import random

nums = [int(i) for i in input().split()]
ans = 0
even = 0

for i in range(3):
    if nums[i]%2 == 0:
        even+=1

if even==3:
    pass
elif even==2:
    for i in range(3):
        if nums[i]%2==0:
            nums[i]+=1
    ans+=1

elif even==1:
    for i in range(3):
        if nums[i]%2==1:
            nums[i]+=1
    ans+=1
else:
    pass

goal_num = max(nums)
ans += (3*goal_num-sum(nums))//2
print(ans)
