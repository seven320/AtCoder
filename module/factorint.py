#encoding:utf-8

#素因数分解
import collections
import time
from tqdm import tqdm

mod = 10**9+7
# 単純な試し割法より早い．
#　探索オーダーはO（logN）のはず．
def primes(n): #試し割り法で各素因数とその指数を求める
    cnt=collections.defaultdict(int)
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            while n%i==0:
                cnt[i]+=1
                n//=i
    if n!=1:
        cnt[n]+=1
    return cnt

print(primes(mod))
