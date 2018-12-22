#encoding utf-8

n = int(input())
answer = ""

def kenzan(ans):
    val = 0
    ans.reverse()
    for i in range(len(ans)):
        val += answer[i]*(-2)**i
    return int(val)

i = 1

while(n != 0):
    if n % 2 == 0:
        answer = "0" + answer
    else:
        answer = "1" + answer
        n -= 1
    n /= -2
if answer == "":
    answer = 0
print(answer)
# print(kenzan(answer))
