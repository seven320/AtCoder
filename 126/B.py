# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

S = str(input())

if 0 < int(S[0:2]) < 13 and 0 < int(S[2:]) < 13:
    ans = "AMBIGUOUS"
elif 0 < int(S[:2]) < 13:
    ans = "MMYY"
elif 0 < int(S[2:]) < 13:
    ans = "YYMM"
else:
    ans = "NA"

print(ans)
