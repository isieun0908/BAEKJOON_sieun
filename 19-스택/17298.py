def main():
    N = int(input())

    A = []
    for i in range(N):
        inputData = int(input().split())
        A.append(inputData)

    for i in range(N):
        a = A[i]
        for j in range(i, N):
            if a < A[j]:
                print(A[j], end=' ')
            break

if __name__ == "__main__":
    main()