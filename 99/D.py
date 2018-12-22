#encoding :utf-8
#encoding utf8

n = int(input())
a = [int(i) for i in input().split()]
dp = [0]

for i in range(len(a)):
    dp.append(max(dp[i],dp[i]+a[i]))

print(dp)


# print(dp)
