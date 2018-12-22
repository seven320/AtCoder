#encoding utf-8
from collections import Counter
def main(n,v):
    odd = Counter(v[0::2]).most_common(2) + [(0,0)]
    even = Counter(v[1::2]).most_common(2) + [(0,0)]

    if odd[0][0] == even[0][0]:
        ans = min(n-odd[0][1]-even[1][1],
        n-odd[1][1]-even[0][1])
    else:
        ans = n-odd[0][1]-even[0][1]
    print(ans)


if __name__ == "__main__":
    n = int(input())
    v = list(int(i) for i in input().split())
    main(n,v)
