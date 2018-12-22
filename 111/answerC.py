from collections import Counter
def main(n,v):
    # n = int(input())
    # v = list(map(int, input().split()))
    odd = Counter(v[0::2]).most_common(2) + [(0, 0)]
    even = Counter(v[1::2]).most_common(2) + [(0, 0)]

    n_half = int(n / 2)

    if (len(odd) == 1 and len(even) == 1) and odd[0][0] == even[0][0]:
        print("aa")
        ans = n_half
    elif odd[0][0] == even[0][0]:
        ans = min(n_half - odd[0][1] + n_half - even[1][1],\
                n_half - odd[1][1] + n_half - even[0][1])
    else:
        ans = n_half - odd[0][1] + n_half - even[0][1]

    print(ans)
    # return ans

if __name__ == "__main__":
    n = int(input())
    v = list(map(int, input().split()))
    main(n,v)
