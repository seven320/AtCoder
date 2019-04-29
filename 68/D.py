# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math


K = int(input())

N = 50
cnt = 0
ans_count = [0 for i in range(N)]
if K//N > 0:
    cnt = K//N
    for i in range(N):
        ans_count[i] = cnt
rest =K-cnt*N
for i in range(rest):
    ans_count[i] += 1

ans = [0 for i in range(N)]
for i in range(N):
    L = ans_count[i]
    ans[i] = (L+1)*(N+1)-2-K

print(N)
for i in range(N):
    print(ans[i],end=" ")

print()




'''
K回操作がある
そのうちじぶんが操作される回数をLとすると
L*N
それ以外はKーL
よって今の数がN-1とすると
元の数は
N-1＋L*N-K+L
=(L+1)*(N+1)-2-K


K=10
N = 3
L=3,3,4
3-1+3*3-10+3 = 4
4
8

4 4 8
5 5 5
1 6 6
2 3 7
3 4 4
'''




#
# 3
#
# 2 2 2
# 5 1 1
# 8 0 0
#
# N
# N-1+(N*(N-1)) 0 0 0 0
#
# N-1 N-1 N-1
#
#
#
# 3
# 8 0 0
#
#
# 4
# 3+12 0 0 0
# 15 0 0 0
# 11 1 1 1
# 7 2 2 2
# 3 3 3 3
#
#
# 5
# 24 0 0 0 0
# 19 1 1 1 1
# 14 2 2 2 2
# 9 3 3 3 3
# 4 4 4 4 4
