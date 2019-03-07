import itertools


def solve(n,a,b,c,ln):
    ans = 10**10
    for l in itertools.product([0, 1, 2, 3], repeat = n):
        if 1 in l and 2 in l and 3 in l:
            count = [0] * 3
            total = [0] * 3
            for i, li in enumerate(l):
                if li != 0:
                    count[li-1] += 1
                    total[li-1] += ln[i]
            cost = 0
            cost += abs(a - total[0]) + 10 * (count[0] - 1)
            cost += abs(b - total[1]) + 10 * (count[1] - 1)
            cost += abs(c - total[2]) + 10 * (count[2] - 1)
            if ans > cost:
                ans = cost
    return ans

def main():
    n, a, b, c = map(int ,input().split())
    ln = [int(input()) for _ in range(n)]

    print(solve(n,a,b,c,ln))

if __name__=="__main__":
    main()
