#encoding utf-8

n = int(input())

withdraw_list = []
withdraw_list.append(1)
# 6
count = 0
while (1):
    count += 1
    if 6**count <=10**5:
        withdraw_list.append(6**count)
    else:
        break
count = 0
while (1):
    count += 1
    if 9**count <=10**5:
        withdraw_list.append(9**count)
    else:
        break
withdraw_list.sort()
withdraw_list.reverse()
# print(withdraw_list)

wi_cou = 0
while (1):
    for i in range(len(withdraw_list)):
        if n == 14:
            wi_cou +=4
            n = 0
            break
        if n == 13:
            wi_cou += 3
            n = 0
            break
        if withdraw_list[i] <= n:
            n -= withdraw_list[i]
            wi_cou += 1
            # print(withdraw_list[i])
            break

    if n == 0:
        break

print(wi_cou)
