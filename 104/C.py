#encoding:utf-8

D, Goal = map(int, input().split())
p = []
c = []
for i in range(D):
    p_tmp, c_tmp = map(int, input().split())
    p.append(p_tmp)
    c.append(c_tmp)

def check_pro(pro_count, p, c):
    sum_val = 0
    


    return sum_val

for i in range(sum(p)):
    sum_val = check_pro(i+1, p, c)
    if sum_val >= Goal:
        print(i+1)
        break
