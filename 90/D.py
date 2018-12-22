#encoding utf-8

n, k = map(int, input().split())

count = 0
if k == 0:
    count = n**2
else:
    for i in range(k, n+1):
        count += int(n/i)*(i-k)
        if (n%i-k >= 0):
            count += n%i-k+1
print(count)
