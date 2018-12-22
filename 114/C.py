#encoidng utf-8

n = int(input())

for i in range(10):
    if 10**i > n:
        break
max_digit = i
# print(max_digit)
num_list = list("753")

def check(nums):
    value = False
    nums_list = list(str(nums))
    # print(nums)
    if (str(3) in nums_list) and (str(5) in nums_list) and (str(7) in nums_list):
        if nums <= n:
            value = True
            # print("::::clear")
    return value

def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out

#指定された桁数においてNより小さい数字の７５３を探す
def find_num(digit):
    count = 0
    for i in range(1,3**(digit)):

        pre_3 = Base_10_to_n(i,3)
        pre_3 = int(pre_3)
        # print(type(pre_3))
        meta='{0:0'+str(digit)+'d}'
        pre_3 = meta.format(pre_3)
        # print(pre_3)
        pre_3_list = list(pre_3)
        predict_num = []
        # print(pre_3_list)1234
        for i in range(len(pre_3_list)):
            if pre_3_list[i] == "0":
                predict_num.append("3")
            elif pre_3_list[i] == "1":
                predict_num.append("5")
            else:
                predict_num.append("7")
        # print("".join(predict_num))
        nums_pre = "".join(predict_num)
        if check(int(nums_pre)):
            count += 1
    return count

count = 0
for i in range(3,max_digit+1):
    count += find_num(i)
print(count)
