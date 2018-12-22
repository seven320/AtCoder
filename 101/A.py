#encoding: utf-8

a=input()

count=0

for i in range(len(a)):
    if a[i]=="+":
        count+=1
    else:
        count-=1
print(count)
