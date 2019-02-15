# encoding:utf-8
import copy
import numpy as np
import random

T = int(input())
S = []
for i in range(T):
    S.append(list(str(input())))

def solve(tape):
    ans = 0
    i = 0
    position = []
    for i in range(len(tape)-4):
        # print(tape[i:i+5])
        if tape[i:i+5]==list("tokyo") or tape[i:i+5]==list("kyoto"):
            position.append([i,i+4])
    position.sort(reverse=True,key=lambda x:x[1])
    now = len(tape)+10
    # print(position)
    for i in range(len(position)):
        if now>position[i][1]:
            ans += 1
            now = position[i][0]

    return ans

for i in range(T):
    print(solve(S[i]))
