#encoding utf-8

n = list(str(input()))

for i in range(len(n)):
    if n[i] == "1":
        n[i] = "to9"
    if n[i] == "9":
        n[i] = "to1"

for i in range(len(n)):
    if n[i] == "to9":
        n[i] = "9"
    elif n[i] == "to1":
        n[i] = "1"

print("".join(n))
