import traceback

def f1(a,b):
    return f2(a) + f2(b)


def f2(x):
    return 1.0 / x

try:
    print(f1(1,0))

except:
    traceback.print_exc()

print("hoge")
