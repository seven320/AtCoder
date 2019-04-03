# encoding:utf-8
import copy
import numpy as np
import random


s = list(str(input()))

dna = ["A","T","G","C"]
count = 0
ans = 0
for i in s:
    if i in dna:
        count += 1
    else:
        count = 0
    ans = max(count,ans)

print(ans)
