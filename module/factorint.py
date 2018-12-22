#encoding:utf-8

#素因数分解
from collections import Counter

def factorint(N):
    table = []
    while(N > 1):
        for i in range(2,N+1):
            if N%i == 0:
                while N%i == 0:
                    N = N//i
                    table.append(i)
                break
    table_ = Counter(table)
    print(table_)
    return table_
