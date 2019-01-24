#encoding:utf-8

A,B,C = map(int,input().split())


if A+B >= C:
    max = B+C

elif A+B < C:
    max = A+2*B+1

print(max)
