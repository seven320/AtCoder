#encoding utf-8
x = int(input())

exp_list = [1]
for i in range(2,33):
    j = 2
    while(i**j <= 1000):
        exp_list.append(i**j)
        j += 1

exp_list.sort()
in_list = [i for i in exp_list if i <= x]
print(in_list[-1])
