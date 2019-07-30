import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

H,W = map(int,input().split())
S = [[] for i in range(H)]
for i in range(H):
    S[i] = list(str(input()))

lights = [[(0,0) for j in range(W)] for i in range(H)]

def count_ver(i,j):
    cnt = 0
    for x in range(i,W):
        if S[j][x] == ".":
            cnt += 1
        else:
            break
    for x in range(i,i+cnt):
        ver,hor = lights[j][x]
        lights[j][x] = (cnt,hor)
    return cnt


def count_hor(i,j):
    cnt = 0
    for y in range(j,H):
        if S[y][i] == ".":
            cnt += 1
        else:
            break
    for y in range(j,j+cnt):
        ver,hor = lights[y][i]
        lights[y][i] = (ver,cnt)
    return cnt

ans = -1
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            ver,hor = lights[i][j]
            if ver == 0:
                ver = count_ver(j,i)
            if hor == 0:
                hor = count_hor(j,i)
            ans = max(ans,hor+ver-1)

print(ans)
