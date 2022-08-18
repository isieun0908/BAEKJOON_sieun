def main():
    N, M = map(int, input().split())

    numList = list(map(int, input().split()))
    for n in range(1, N):       # 누적 합 리스트 생성
        numList[n] += numList[n-1]
    numList = [0]

    for m in range(0, M):       # 테스트 케이스 M
        i, j = map(int, input().split())    # 입력

        index = i - 2
        if index < 0:
            print(numList[j-1])
        else:
            print(numList[j-1] - numList[index])

if __name__ == "__main__":
    main()