# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7



H,W = map(int,input().split())
area = H*W

ans = mod

if area % 3 == 0:
    ans = 0
    print(ans)
    exit()

for i in range(1,H):
    h = H - i
    max_area = max(i*W,(h//2)*W,(h-h//2)*W)
    min_area = min(i*W,(h//2)*W,(h-h//2)*W)
    ans = min(max_area-min_area,ans)

    w = W
    max_area = max(i*W,(w//2)*h,(w-w//2)*h)
    min_area = min(i*W,(w//2)*h,(w-w//2)*h)
    ans = min(max_area-min_area,ans)

H,W = W,H
for i in range(1,H):
    h = H - i
    max_area = max(i*W,(h//2)*W,(h-h//2)*W)
    min_area = min(i*W,(h//2)*W,(h-h//2)*W)
    ans = min(max_area-min_area,ans)

    w = W
    max_area = max(i*W,(w//2)*h,(w-w//2)*h)
    min_area = min(i*W,(w//2)*h,(w-w//2)*h)
    ans = min(max_area-min_area,ans)


print(ans)
