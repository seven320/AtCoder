#encoding utf-8

s = list(input())

count = []
code_pass = False
if s[0] == "A":
    capital_count = 0
    for i in range(len(s)):
        # print(s[i])
        if "C" == s[i]:
            count.append(i)
            # print(count)

        if s[i].isupper():
            capital_count += 1
            # print(capital_count)

    if len(count) == 1 and 2 <= count[0] <= len(s)-2:
        if capital_count == 2:
            code_pass = True

if code_pass == True:
    print("AC")
else:
    print("WA")
