# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N, M, K = LI()
AB = []
CD = []
for i in range(M):
    a,b = LI()
    a -= 1
    b -= 1
    AB.append([a,b])
for k in range(K):
    c, d = LI()
    c -= 1
    d -= 1
    CD.append([c,d])

direct_friend = {}
blocked = {}
relation = [[] for i in range(N)]
for i in range(N):
    direct_friend[i] = []
    blocked[i] = []
for i in range(M):
    a,b = AB[i]
    direct_friend[a].append(b)
    direct_friend[b].append(a)
for i in range(K):
    c,d = CD[i]
    blocked[c].append(d)
    blocked[d].append(c)

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

u = UnionFind(N)
for a,b in AB:
    u.Unite(a, b)

minus_cnt = [0 for i in range(N)]
for a,b in AB:
    minus_cnt[a] += 1
    minus_cnt[b] += 1


for c, d in CD:
    if u.isSameGroup(c,d):
        minus_cnt[c] += 1
        minus_cnt[d] += 1
for i in range(N):
    print(u.Count(i) - 1 - minus_cnt[i], end = " ")

print("")

"""
direct_friend = {}
blocked = {}
relation = [[] for i in range(N)]
for i in range(N):
    direct_friend[i] = []
    blocked[i] = []
for i in range(M):
    a,b = AB[i]
    direct_friend[a].append(b)
    direct_friend[b].append(a)
for i in range(K):
    c,d = CD[i]
    blocked[c].append(d)
    blocked[d].append(c)

def dfs(node, p, cluster):
    cluster.append(node)
    if len(direct_friend[node]) == 1:
        return cluster
    for new_node in direct_friend[node]:
        if new_node == p:continue
        elif new_node in cluster:continue
        else:
            return dfs(new_node, node, cluster)

for i in range(N):
    if len(relation[i]) == 0:
        cluster = dfs(i, -1, [])
        # print(cluster)
        if cluster == None:
            relation[i] = []
        else:   
            for j in cluster:
                relation[j] = cluster

# print(relation)
# print(direct_friend)
# print(blocked)

for i in range(N):
    blocked[i] = set(blocked[i])
    direct_friend[i] = set(direct_friend[i])

# for i in range(N):
#     if len(direct_friend[n]) == 0:

ans = []
for n in range(N):
    ans.append(len(set(relation[n]) - direct_friend[n] - blocked[n] - set([n])))

for a in ans:
    print(a, end = " ")
print("")

"""


