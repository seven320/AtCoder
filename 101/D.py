#encoding:utf-8
k=int(input())
a=[]

def sunuke(N):
    sn=0
    n=str(N)
    for i in range(len(n)):
        sn+=int(n[i])
    return N/sn

for i in range(1,100):
    a.append([i,sunuke(i)])
    if len(a)>=k:
        max=0
        for j in range(len(a)):
            if max<=a[j][1]:
                max=a[j][1]
        if max>=sunuke(i):


#print
for i in range(k):
    print(a[i][0])
