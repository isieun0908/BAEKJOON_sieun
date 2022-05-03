def main():
    N, K = map(int, input().split())

    n_fac = 1
    for i in range(2, N+1):
        n_fac *= i
    k_fac = 1
    for i in range(2, K+1):
        k_fac *= i
    n_k_fac = 1
    for i in range(2, N-K+1):
        n_k_fac *= i
    print(int(n_fac / (k_fac * n_k_fac)))

if __name__ == "__main__":
    main()