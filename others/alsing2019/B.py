#encoding:utf-8

N = int(input())
A,B = map(int, input().split())
P = [int(i) for i in input().split()]

P.sort()
a_count = len([i for i in P if i<= A])
b_count = len([i for i in P if A < i <= B])
c_count = len([i for i in P if B < i])

print(min(a_count,b_count,c_count))
