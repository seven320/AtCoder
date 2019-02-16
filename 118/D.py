# encoding:utf-8
import copy
import numpy as np
import random

n,m = map(int,input().split())
a = [int(i) for i in input().split()]

translate_match=[2,5,5,4,5,6,3,7,6]
match = []
for i in range(m):
    match.append(translate_match[a[i]-1])

def dp(amari,memory):
    for i in range(len(match)):
        if amari==match[i]:
            print(memory)
            break
        elif amari>match[i]:
            next = amari-match[i]
            memory[i] += 1
            dp(next,memory)

memory = [0 for i in range(len(match))]
print(dp(n,memory))
