import math

def main():
    N = int(input())
    A = list(map(int, input().split()))

    M = int(input())
    T = list(map(int, input().split()))

    A.sort()

    for t in T:
        flag = 0
        half = math.floor(N/2)
        while True:
            if A[half] == t:
                flag = 1
                break
            elif t > A[half]:
                half = half + math.floor(half/2)
            else:
                if half == 0: half = -1
                else: half = math.floor(half/2)
            if half < 0 or half >= N:
                break
        if flag: print(1)
        else: print(0)

if __name__ == "__main__":
    main()