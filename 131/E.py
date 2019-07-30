# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

N,K = LI()

if K > (N-1)*(N-2)//2 :
    print("-1")
    exit()
nodes = []
for i in range(1,N):
    nodes.append([1,i+1])
add = (N-1)*(N-2) // 2 - K
for i in range(N-2):
    for j in range(i,N-2):
        add -= 1
        if add < 0:
            break
        nodes.append([i+2,j+3])
    else:
        continue
    break

print(len(nodes))
for node in nodes:
    x,y = node
    print(x,y)
