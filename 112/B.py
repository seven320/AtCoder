#encoding utf-8
from operator import itemgetter


n,t = map(int, input().split())

ct = []
for i in range(n):
    c_0,t_0 = map(int, input().split())
    ct.append([c_0,t_0])

time_flag = 0
for i in range(len(ct)):
    if ct[i][1] <= t:
        time_flag += 1
    else:
        ct[i][0] = 1001

ct0=list(ct)
ct.sort(key=itemgetter(0))
# print(ct)

if time_flag == 0:
    print("TLE")
else:
    print(ct[0][0])
