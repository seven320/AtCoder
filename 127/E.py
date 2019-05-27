# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N,M,K = map(int,input().split())

def mCn(m,n):
    return math.factorial(m)//(math.factorial(n)*math.factorial(m-n)) % mod

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

N1 = 10**6
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N1 + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


ans = 0
for i in range(1,M):
    ans += (M-i)*N**2*i*(cmb(M*N-2,K-2,mod))
    if ans > mod:
        ans = ans % mod

for i in range(1,N):
    ans += (N-i)*M**2*i*(cmb(M*N-2,K-2,mod))
    if ans > mod:
        ans = ans % mod

print(ans)
