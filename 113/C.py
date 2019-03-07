#encoding:utf-8

n,m = map(int, input().split())
P = []
Y = []
city_tb = []
for i in range(m):
    p,y = map(int,input().split())
    P.append(p)
    Y.append(y)
    city_tb.append([p,y])

city_tb_ = sorted(city_tb,key=lambda x:x[1])
# print(city_tb_)

count_cities = [0 for i in range(n+1)]
city_cla = {}
for i in range(m):
    count_cities[city_tb_[i][0]] += 1
    city_cla[str(city_tb_[i][0])+str(city_tb_[i][1])]='{:06d}'.format(city_tb_[i][0])+'{:06d}'.format(count_cities[city_tb_[i][0]])

for i in range(m):
    print(city_cla[str(P[i])+str(Y[i])])
