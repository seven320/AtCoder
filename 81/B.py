#encoding:utf-8



N = int(input())
A = [int(i) for i in input().split()]

answer = 100
for i in range(N):
    count = 0
    while A[i]%2 == 0:
        count += 1
        A[i] /= 2
    answer = min(answer,count)

print(answer)
