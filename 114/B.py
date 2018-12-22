#encoding utf-8

s = str(input())


nums = list(s)
b = 753

diff = b

for i in range(len(nums)-2):
    predict = int("".join(nums[i:i+3]))
    if abs(b-predict) < diff:
        diff = abs(b-predict)

print(diff)
