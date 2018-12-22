#encoding utf-8

a, b = map(int, input().split())

count = 0
for i in range(a,b+1):
    num = list(str(i))
    kaibun = 0
    for j in range(int(len(num)/2)):
        if num[j] == num[len(num)-j-1]:
            kaibun += 1
    if kaibun == int(len(num)/2):
        count += 1

print(count)
