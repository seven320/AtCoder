#encoding utf-8

a,b,k = map(int, input().split())
# print(a,b,k)

for i in range(k):
    if i%2 == 0:
        if a%2 == 1:
            a -= 1
        b += int(a/2)
        a = int(a/2)
    # turn b
    else:
        if b%2 == 1:
            b -= 1
        a += int(b/2)
        b = int(b/2)



print(a,b)
