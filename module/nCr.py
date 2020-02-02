#逆元を使ったnCrの計算

mod = 10 ** 9 + 7
n_ = 10 ** 5 + 3 # まで対応


fun = [1 for i in range(n_+1)]
for i in range(1, n_ + 1):
    fun[i] = fun[i-1] * i % mod

rev = [1 for i in range(n_+1)]
rev[n_] = pow(fun[n_], mod-2, mod)
for i in range(n_-1,0,-1):
    rev[i] = rev[i+1]*(i+1) % mod

def nCr(n,r):
    if n <= 0 or r < 0 or r> n:return 0
    return fun[n]*rev[r]%mod*rev[n-r]%mod
