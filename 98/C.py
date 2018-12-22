#encoding utf-8

n = int(input())
s = list(str(input()))

reverse = 3*10**5+1
west = []
east = []
west_num = 0
east_num = 0
for i in range(len(s)):
    if s[i] == "W":
        west_num += 1
    elif s[i] == "E":
        east_num += 1
    west.append(west_num)
    east.append(east_num)
# print(west,east)
for i in range(n):
    if i == 0:
        point = east[-1]+east[0]
    elif i == n-1:
        point = west[i-1]
    else:
        point = east[-1]-east[i]+west[i-1]
    # print(point)
    reverse = min(point, reverse)

print(reverse)
