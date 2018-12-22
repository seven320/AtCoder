#encoding utf-8
#
# n, m = map(int, input().split())
# a = [int(i)%m for i in input().split()]
#
# count = 0
# for i in range(n):
#     candy = a[i]
#     if candy % m == 0:
#         count += 1
#     for rest in range(1,n-i):
#         candy += a[i+rest]
#         if candy % m == 0:
#             count += 1
#
# print(count)
N, M = map(int, input().split())
*A, = map(int, input().split())
C = {0: 1}
ans = 0
s = 0
for a in A:
    s = (s + a) % M
    ans += C.get(s, 0)
    C[s] = C.get(s, 0) + 1
    print(C)
print(ans)
