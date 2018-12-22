#encoding utf-8
num = list(int(i) for i in input().split())

num.sort(reverse=True)

max = int(str(num[0])+str(num[1]))+num[2]

print(max)
