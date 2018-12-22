#encoding: utf-8

n,k=map(int,input().split())

a=[int(i) for i in input().split()]

for i in range(len(a)):
    if a[i]==1:
        num=i
count=0
num0=num
num1=num
#up
while(1):
    num+=(k-1)
    count+=1
    if num>=n:
        num0-=num-n
        break

while(1):
    if num0<=1:
        break
    num0-=(k-1)
    count+=1
count2=0
num01=num1
while(1):
    num01-=(k-1)
    count2+=1
    if num01<=1:
        num1+=1-num01
        break
while(1):
    if num1>=n:
        break
    num1+=(k-1)
    count2+=1
print(min(count,count2))
