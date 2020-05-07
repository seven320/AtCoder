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
H = LI()
route = []
for i in range(M):
    a, b = LI()
    a -= 1
    b -= 1
    route.append((a,b))

N_path = [[] for i in range(N)]
for a, b in route:
    N_path[a].append(b)
    N_path[b].append(a)

# print(H)
ans = 0
for i in range(N):
    for path in N_path[i]:
        if H[path] >= H[i]:
            break
    else:
        ans += 1
print(ans)



# uf = UnionFind(N)
# for a, b in route:
#     uf.Unite(a, b)

# ans = 0
# good_obs = []
# for i in range(N):
#     print(good_obs)
#     if len(good_obs) == 0:
#         good_obs.append(i)
#     else:
#         for obs in good_obs:
#             print(obs, i)
#             if uf.isSameGroup(obs, i):
#                 if H[obs] == H[i]:
#                     good_obs.append(i)
#                     break
#                 elif H[obs] > H[i]:
#                     pass
#                 elif H[obs] < H[i]:
#                     good_obs.remove(obs)
#                     good_obs.append(i)
# print(good_obs)
# print(len(good_obs))
                
            
    