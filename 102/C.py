# encoding: utf-8

#input
n = int(input())
A = [int(i) for i in input().split()]
# print(A)
def sad_value(A,b):
    sadness = 0
    for i in range(len(A)):
        sadness += abs(A[i]-b-i-1)
    return sadness
A_i = []
for i in range(len(A)):
    A_i.append(A[i]-i)
A_i.sort()
sadness = []
for i in range(5):
    a = int(n/2)
    sadness.append(sad_value(A, A_i[a]-2+i))
sadness.sort()
print(sadness[0])
