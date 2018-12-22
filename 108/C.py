# encoding utf 8

n, k = map(int, input().split())

sum = 0
for i in range(1,n+1):
    if 2*i%k == 0:
        # print(sum)
        sum += 1

        max = int((n-i)/k)
        # print("i",i,"max",max)
        if max == 1:
            sum += 6
        elif max>1:
            sum += max*(1+max)/2*6

print(int(sum))
