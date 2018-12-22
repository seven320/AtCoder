#encoding utf:8

n = int(input())
# num=[]
num = list(int(i) for i in input().split())
# for i in range(n):
#     num.append(int(input().split()))

#gcd 最大公約数
def gcd(a,b):
    gcd = 1
    list_a = []
    list_b = []
    for i in range(a):
        if a % (i+1) ==0:
            a = a/(i+1)
            list_a.append(i+1)
    for i in range(b):
        if b % (i+1) ==0:
            b = b/(i+1)
            list_b.append(i+1)
    # print(list_a,list_b)
    for num in range(len(list_a)):
        if list_a[num] in list_b:
            gcd = gcd * list_a[num]
    return int(gcd)

# lcm: 最小公倍数
def lcm(a,b):
    lcm = a*b/gcd(a,b)
    return int(lcm)

for i in range(n):
    if i == 0:
        a_lcm = lcm(num[0], num[1])
    a_lcm = lcm(a_lcm,num[i])

max = a_lcm-1
f=0
for i in range(len(num)):

    f += (max%num[i])
print(f)
