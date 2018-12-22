#encoding:utf-8

n = list(input())

count = 0
for i in range(4):
    if n[i] == "2":
        count += 1


print(count)
