# encoding utf-8

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a.sort()

min = []
max = []

for i in range(len(a)):
    min.append(a[0])
    max.append(a[-1])
