#encoding: utf-8

N = int(input())

def sum_digit(num):
    list_num = [int(x) for x in list(str(num))]
    sum = 0
    for i in range(len(list_num)):
        sum += list_num[i]

    return sum

def expect(N):
    digit = len(str(N))

    l_num = [int(x) for x in list(str(N))]
    sum_a = l_num[0]
    # print(l_num)
    # print(l_num[digit-1])
    b = (N-int(l_num[0])*10**(digit-1))
    if digit == 1:
        sum = N
    elif N == 100:
        sum =10
    elif N == (10 or 1000 or 10**5):
        sum = 10

    elif b==0:
        sum_a = int(N/2)
        sum = sum_digit(sum_a)
        sum = sum*2
        for i in range(digit):
            # print("goaho",i)
            # print("hi")
            if sum > (sum_digit(N-10**i)+1):
                # print("hi")
                sum = sum_digit(N-10**i)+1
    else:
        sum_b = sum_digit(b)
        sum = sum_a+sum_b

    return sum

print(expect(N))
