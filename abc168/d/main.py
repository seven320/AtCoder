#!/usr/bin/env python3
# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections
from decimal import Decimal # 10進数で考慮できる

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

"""
N rooms
M paths

0 room is start
"""
class UnionFind():
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        self.root = [-1]*(n+1)
        # 木をくっつける時にアンバランスにならないように調整する
        self.rnk = [0]*(n+1)

    # ノードxのrootノードを見つける
    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            # ここで代入しておくことで、後の繰り返しを避ける
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    # 木の併合、入力は併合したい各ノード
    def Unite(self, x, y):
        # 入力ノードのrootノードを見つける
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        # すでに同じ木に属していた場合
        if(x == y):
            return 
        # 違う木に属していた場合rnkを見てくっつける方を決める
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # rnkが同じ（深さに差がない場合）は1増やす
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    # xとyが同じグループに属するか判断
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # ノードxが属する木のサイズを返す
    def Count(self, x):
        return -self.root[self.Find_Root(x)]

N, M = LI()
AB = []
for i in range(M):
    a,b = LI()
    a -= 1
    b -= 1
    AB.append((a,b))

paths = {}
for i in range(N):
    paths[i] = []
for a, b in AB:
    paths[a].append(b)
    paths[b].append(a)

# uf = UnionFind(N)
# for a,b in AB:
#     uf.Unite(a,b)

# ans = True
# for i in range(N):
#     if not uf.isSameGroup(0, i):
#         ans = False

# if ans == False:
#     print("No")
#     sys.exit()

q = collections.deque()

# node No, parent No
q.append((0, -1))

# 検索するんではなくて，尋ねたかどうかの0,1のlistを持っておいてそこに保存していく．

anss = [0 for i in range(N)]
rooms = [0 for i in range(N)]
rooms[0] = 1
while len(q) > 0:
    node, p = q.popleft()

    for path in paths[node]:
        if path == p:
            continue
        if rooms[path]: # すでに探索済み
            continue
        q.append((path, node))
        rooms[path] = 1
        anss[path] = node
print("Yes")
for ans in anss[1:]:
    print(ans + 1)


