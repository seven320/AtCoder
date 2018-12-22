#encoding utf-8

import numpy as np

N, M, Q = map(int, input().split())

rail = []
for i in range(M):
    r = list(map(int, input().split()))
    rail.append(r)


query = []

for i in range(Q):
    q = list(map(int, input().split()))
    query.append(q)

f = np.zeros((N, N))
for i in range(M):
    f[rail[i][0]-1][rail[i][1]-1] += 1

C = np.zeros((N, N))
for i in range(N):
    j = 0
    while j + i < N:
        if i == 0:
            C[j][j+i] = f[j][j+i]
        else:
            C[j][j+i] = f[j][j+i] + C[j+1][j+i] + C[j][j+i-1] - C[j+1][j+i-1]
        j += 1
# print(C)

for i in range(Q):
    print(int(C[query[i][0]-1][query[i][1]-1]))
