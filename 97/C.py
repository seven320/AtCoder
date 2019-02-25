#encoding utf-8

import copy
import numpy as np
import random


s = list(str(input()))
k = int(input())

substrings = []
for length in range(1,len(s)+1):
    if length > 5:
        break
    for i in range(len(s)-length+1):
        word = "".join(s[i:i+length])
        # print(word)
        if word in substrings:
            pass
        else:
            substrings.append(str(word))

substrings.sort()
# print(substrings)
print(substrings[k-1])
