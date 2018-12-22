#encoding:utf-8

N = int(input())
t,a = map(int,input().split())
h = list(map(int, input().split()))
# print(h)

diff = 10000
for i in range(N):
    tem_diff = abs(t-h[i]*0.006-a)
    if tem_diff < diff:
        diff = tem_diff
        place = i+1


print(place)
