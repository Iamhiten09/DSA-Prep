import sys
MOD = 10 ** 9 + 7

def modinv(x):
    return pow(x, MOD - 2, MOD)

def mat_mult(A, B):
    n = len(A)
    m = len(B[0])
    l = len(B)
    res = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(l):
                res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
    return res

def mat_pow(mat, power):
    n = len(mat)
    res = [[int(i == j) for j in range(n)] for i in range(n)]
    while power:
        if power % 2:
            res = mat_mult(res, mat)
        mat = mat_mult(mat, mat)
        power //= 2
    return res

def get_ans(n, k, a, p):
    # Normalize p to get transition matrix as fractions
    # We'll keep numerators and denominators separately
    # p[i][j] = numerator[i][j] / row_sum[i]
    numer = [[p[i][j] for j in range(n)] for i in range(n)]
    denom = [sum(p[i]) for i in range(n)]

    # We want to work with numerators and denominators
    # Let's build the transition matrix as numerators and a global denominator
    # We'll use a common denominator: prod(denom)
    from math import gcd
    from functools import reduce
    def lcm(x, y):
        return x * y // gcd(x, y)
    common_denom = reduce(lcm, denom)

    # Build transition matrix T[i][j] = numer[i][j] * (common_denom // denom[i])
    T = [[0] * n for _ in range(n)]
    for i in range(n):
        mul = common_denom // denom[i]
        for j in range(n):
            T[i][j] = numer[i][j] * mul % MOD

    # Initial state: start at city 0
    state = [[0] for _ in range(n)]
    state[0][0] = 1

    # Exponentiate transition matrix
    T_k = mat_pow(T, k)
    # Final state probabilities (numerators, denominator is common_denom^k)
    final_state = mat_mult(T_k, state)

    # Expected value numerator: sum(final_state[i][0] * a[i])
    expected_num = 0
    for i in range(n):
        expected_num = (expected_num + final_state[i][0] * a[i]) % MOD
    # Denominator is common_denom^k
    expected_den = pow(common_denom, k, MOD)

    # Output expected_num * modinv(expected_den) % MOD
    return expected_num * modinv(expected_den) % MOD

def main():
    n = int(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())
    a = []
    for _ in range(n):
        a.append(int(sys.stdin.readline().strip()))
    p = []
    for _ in range(n):
        p.append(list(map(int, sys.stdin.readline().strip().split())))
    result = get_ans(n, k, a, p)
    print(result)

if __name__ == "__main__":
    main()