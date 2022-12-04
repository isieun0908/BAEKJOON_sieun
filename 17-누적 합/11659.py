import sys

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())

    numList = list(map(int, sys.stdin.readline().rstrip().split()))

    sum_of_intervals = [0]
    sum = 0
    for i in range(N):
        sum += numList[i]
        sum_of_intervals.append(sum)

    for m in range(M):       # 테스트 케이스 M개
        i, j = map(int, sys.stdin.readline().rstrip().split())    # 입력

        print(sum_of_intervals[j] - sum_of_intervals[i-1])

if __name__ == "__main__":
    main()