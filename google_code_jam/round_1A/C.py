# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import math

T = int(input())
N = []
W = []

for t in range(T):
    n = int(input())
    w = []
    for i in range(n):
        w = w+[str(input())]
    W.append(w)


def solve(words):
    n = len(words)
    table = [[0 for i in range(n)] for j in range(n)]
    accents = {}
    for i in range(len(words)):
        for j in range(len(words)):
            if i >= j:
                pass
            else:
                count = 0
                for num in range(1,min(len(words[i]),len(words[j]))+1):
                    if words[i][-num] == words[j][-num]:
                        count += 1
                        if count==min(len(words[i]),len(words[j])):
                            accent = words[i][-num:-1]+words[i][-1]
                            accents[accent] = count
                            # print("hoge")
                    else:
                        if count > 0:
                            accent = words[i][1-num:-1]+words[i][-1]
                            accents[accent] = count
                            # print("huge")
                            break
                        else:
                            break
                table[i][j] = count



    ans_1 = 0
    # print(table)
    # print(accents)
    for i in range(n):
        # print(table)
        if max(table[i])>0:
            del_j = table[i].index(max(table[i]))
            for k in range(n):
                table[k][del_j] = 0
                table[del_j][k] = 0
            ans_1 += 1

    ans = len(accents.keys())
    # print(accents)
    # print(ans,ans_1)
    ans = min(ans,ans_1)*2

    return ans


for i in range(T):
    print("Case #"+str(i+1)+": {0}".format(solve(W[i])))
