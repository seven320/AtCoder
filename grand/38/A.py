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

H,W,A,B = LI()

a_1 = [0 for i in range(H)]
b_1 = [0 for i in range(W)]

a = [0 for i in range(H)]
b = [0 for i in range(W)]

s = [[0 for i in range(W)] for j in range(H)]

for h in range(H):
    for w in range(W):
        a_t = a_1[h] + 1
        b_t = b_1[w] + 1




    #     if min(a_t, H-a_t) <= A and min(b_t, W-b_t) <= B:
    #         a_1[h] += 1
    #         b_1[w] += 1
    #         s[h][w] = 1
    # print(a_1,b_1)


        # if a[h] < A and b[w] < B:
        #     a_1[h] += 1
        #     a[h] = min(a_1[h], H-a_1[h])
        #     b_1[w] += 1
        #     b[w] = min(b_1[w], W-b_1[w])
        #     s[h][w] = 1
for i in range(H):
    print(s[i])






'''
3 3 1 2

100 1
111 0
001 1

111

3 3 1 0
100
100
100

4 4 2 2
1100 2
1100 2
0011 2
0011 2

2222

4 4 2 1
1000
1000
0100
0101

"no"

5 5 2 1
10000
10000
01111
01111
00001

5 5 2 2
11000
11000
00110
00101
00011

00011
00101
01001
10001
00110





5 5 2 0
muri




'''
