def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        a = A[i]
        flag = 1
        for j in range(i, N):
            if a < A[j]:
                flag = 0
                print(A[j], end=' ')
                break
        if flag:
            print(-1, end=' ')

if __name__ == "__main__":
    main()