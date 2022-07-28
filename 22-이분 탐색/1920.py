import math
def main():
    N = int(input())
    A = list(map(int, input().split()))

    M = int(input())
    T = list(map(int, input().split()))

    A.sort()
    print(A)

    for t in range(T):
        flag = 0
        half = math.floor(N/2)
        while half >= 0 or half < N:
            if A[half] == t:
                flag = 1
                break
            half = math.floor(N/2)
        if flag: print(1)
        else: print(0)

if __name__ == "__main__":
    main()