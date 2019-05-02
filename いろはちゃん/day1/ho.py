# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N,A,B = map(int,input().split())
if B == 0:
    D = []
else:
    D = [int(i) for i in input().split()]

D.insert(0,1)
D.insert(B+1,N+1)
D.sort()
# print(D)
ans = 0
date_cnt = 0

if A==1:
    print("0")
    exit()

for b in range(B+1):
    # print((D[b+1]-D[b]))
    if (D[b+1]-D[b])/(A) > 1:
        if (D[b+1]-D[b])/(A) == (D[b+1]-D[b])//(A):
            date_cnt += int((D[b+1]-D[b])/(A)-1)
        else:
            date_cnt += (D[b+1]-D[b])//(A)

ans = N-date_cnt-B
print(ans)
