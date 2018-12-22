#encoding:utf-8

def evennum(number):
    count=0
    while(1):
        if number%2==1:
            break
        else:
            number=number/2
            count+=1
    return count
#input
n=int(input())

l=[int(i) for i in input().split()]

count=0

for i in range(n):
    count+=evennum(l[i])

print(count)
