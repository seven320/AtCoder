#encoding utf-8
import sympy

n,m = map(int, input().split())

#pfs prime factors　素因数
# pfs = sympy.factorint(m)
# print(pfs.keys())


def yakusuu(m):
    num = int(m)
    yakusuu_array = []

    for i in range(1,num):
        if num % i == 0:
            yakusuu_array.append(i)
    yakusuu_array.append(m)
    return yakusuu_array

def DB(count,n,m):
    if str(n)+str(m) in database:
        count = database[str(n)+str(m)]
    else:
    # print(n,m)
        if n == 1:
            count += 1
        elif m == 1:
            count += 1
        else:
            bunkai = yakusuu(m)
            for i in range(len(bunkai)):
                count = DB(count, n-1, int(m/bunkai[i]))
        dababase[str(n)+str(m)] = count
    return count

database = {}
print(DB(0,n,m))
