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

N = int(input())
ab = []
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = LI()
    a -= 1
    b -= 1
    ab.append([a,b])
    G[a].append(b)
    G[b].append(a)

cnt_0, cnt_1, cnt_2 = 0,0,0
for i in range(1,N+1):
    if i % 3 == 0:
        cnt_0 += 1
    elif i%3 == 1:
        cnt_1 += 1
    else:
        cnt_2 += 1
v_0, v_1, v_2 = 3,1,2

def dfs(node, p, cnt,ans):
    if cnt == 3:
        ans.append(node)
        return ans
    for new_node in G[node]:
        if new_node == p:
            continue
        else:
            ans = dfs(new_node, node, cnt + 1, ans)
    return ans

pairs = []
for i in range(N):
    ps = dfs(i, -1, 0, [])
    for p in ps:
        if i > p:
            pairs.append([p, i])
        else:
            pairs.append([i, p])

def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

pairs2 = get_unique_list(pairs)
while cnt_1 > 0 and cnt_2 > 0:
    count_dic = {}
    for i in range(N):
        count_dic[i] = 0
    for pair in pairs2:
        a, b = pair
        count_dic[a] += 1
        count_dic[b] += 1
    sorted_dic = sorted(count_dic.items(), key = lambda x:x[1], reverse= 1)
    node = sorted_dic[0][0]
    if cnt_0 > 0:
        ans[node] = v_0
        v_0 += 3
        cnt_0 -= 1
    else:
        if cnt_1 < cnt_2:
            ans[node] = v_1
            v_1 += 3
            cnt_1 -= 1
        else:
            ans[node] = v_2
            v_2 += 3
            cnt_2 -= 1
    pairs3 = []
    for pair in pairs2:
        if node in pair:
            a,b = pair
            if a == node:
                


