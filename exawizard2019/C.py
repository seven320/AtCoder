# encoding:utf-8
import copy
import numpy as np
import random
import bisect #bisect_left　これで二部探索の大小検索が行える

N,Q = map(int, input().split())
s = str(input())
T = []
D = []
for i in range(Q):
    t,d = map(str,input().split())
    T.append(t)
    D.append(d)

T.reverse()
D.reverse()

nl = 0
nr = N-1
L = []#回収できた分
R = []
for i in range(Q):
    if D[i]=="R":
        if nr >= 0:
            if s[nr] == T[i]:
                L.append(s[nr])
                nr -= 1
        if len(R)>0:
            if R[-1] == T[i]:
                R.pop()
                nl -= 1

    else:
        if nl <= N-1:
            if s[nl] == T[i]:
                R.append(s[nl])
                nl += 1
        if len(L)>0:
            if L[-1] == T[i]:
                L.pop()
                nr -= 1

print(N-len(R)-len(L))



#
# print(N-len(L)-len(R))
