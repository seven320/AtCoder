#encoding:utf-8
#input
n,m=map(int,input().split())
v=[]
x=[]
y=[]
z=[]
for i in range(n):
    x_1,y_1,z_1=map(int,input().split())
    x.append(x_1)
    y.append(y_1)
    z.append(z_1)

def value(list,x,y,z):
    xv=0
    yv=0
    zv=0

    for k in range(len(list)):
        i=list[k]
        xv+=x[i]
        yv+=y[i]
        zv+=z[i]
    return abs(xv)+abs(yv)+abs(zv)

list=[1,3,5]

value=value(list,x,y,z)

print(value)
