#encoding:utf-8

N,Y = map(int,input().split())

for i in range(N+1):
    for j in range(N-i+1):
        if i*9+j*4+N == Y/1000:
            print(i,j,N-i-j)
            exit()

print(-1,-1,-1)
