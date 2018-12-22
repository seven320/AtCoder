#encoding utf-8

n, m = map(int, input().split())

if n == 1 and m == 1:
    reverse = 1
elif n == 1 or m == 1:
    reverse = max(n,m)-2
else:
    reverse = (m-2)*(n-2)

print(reverse)
