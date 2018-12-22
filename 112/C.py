#encoding utf-8

n = int(input())
data = []
for i in range(n):
    x,y,h=map(int,input().split())
    data.append([x,y,h])

def calH(cx,cy,data):
    return data[2]+abs(data[0]-cx)+abs(data[1]-cy)

def conh(temH,cx,cy,data):
    return temH-abs(data[0]-cx)-abs(data[1]-cy)


for i in range(101):
    for j in range(101):
        # clear = 0
        # count = 0
        # for k in range(n):
        #     if clear == 0:
        #         temH = calH(i,j,data[k])
        #         if data[k][2] != 0:
        #             clear = 1
        #         else:
        #             if conh(temH,i,j,data[k]) < 0:
        #                 count += 1
        #             else:
        #                 count += 1
        #                 clear = 1
        #
        # for k in range(count,n):
        #     ignore_flag = 0
        #     if data[k][2] == 0:
        #         if conh(temH,i,j,data[k]) < 0:
        #             ignore_flag = 1
        #             count += 1
        #
        #     if ignore_flag == 0:
        #         if calH(i,j,data[k]) != temH:
        #             break
        #         else:
        #             count += 1
        #     if count == n:
        #         answer=[i,j,calH(i,j,data[0])]
        for k in range(n):
            temH = calH(i,j,data[k])
            if conh(temH,i,j,data[k]) >= 0:
                break
        count = 0
        for k in range(n):
            if conh(temH,i,j,data[k]) < 0:
                pass
                count += 1
            else:
                if calH(i,j,data[k]) == temH:
                    count += 1
                else:pass

        if count == n:
            answer=[i,j,calH(i,j,temH)]

print(answer[0],answer[1],answer[2])
