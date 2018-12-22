#encoding:utf-8
N=str(input())

sn=0

for i in range(len(N)):
    sn+=int(N[i])

if int(N)%sn==0:
    print("Yes")
else:
    print("No")
