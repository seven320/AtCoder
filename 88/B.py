#encoding:utf-8

N = int(input())
A = [int(i) for i in input().split()]

A.sort(reverse=True)
answer = 0
alice = 0
bob = 0
for i in range(len(A)):
    if i % 2 == 0:
        alice += A[i]
    else:
        bob += A[i]

print(alice-bob)
