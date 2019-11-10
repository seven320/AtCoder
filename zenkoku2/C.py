# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
A = LI()
B = LI()


A, B = zip(*sorted(zip(A, B), key=lambda x:x[1]))

A_c = copy.deepcopy(A)

A = sorted(A)
B = sorted(B)

for i in range(N):
    if A[i] > B[i]:
        print("No")
        sys.exit(0)

for i in range(1,N):
    if A[i] < B[i-1]:
        print("Yes")
        sys.exit(0)

# ans = "Yes"
# for i in range(N):
#     if A[i] <= B[i]:
#         pass
#     else:
#         ans = "No"
#         break

si2i = sorted(range(len(A_c)), key=lambda x:A_c[x])
a = 0
count = 0
while True:
    a = si2i[a]
    if a == 0:
        break
    count += 1

if count <= N - 2:
    print("Yes")
else:
    print("No")
