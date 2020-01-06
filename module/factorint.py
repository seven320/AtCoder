#encoding:utf-8

#素因数分解
from collections import Counter
import time
from tqdm import tqdm

N = 10**15
# 単純な試し割法より早い．
#　探索オーダーはO（logN）のはず．
def factorint(N):
    """
    Nを作っている素数を辞書で返す．
    input 100
    output Counter({2: 2, 5: 2})
    """
    table = []
    tmp = 2
    while(N > 1):
        for i in range(tmp,N+1):
            if N%i == 0:
                while N%i == 0:
                    N = N//i
                    table.append(i)
                tmp = i+1
                break
    table_ = Counter(table)
    return table_

print(factorint(100))
