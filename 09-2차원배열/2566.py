import sys
SIZE = 9


def main():
    # max값 정의
    max = 0
    max_index = [0, 0]

    # 입력받으며, max 값 비교
    for i in range(SIZE):
        list_ = list(map(int, sys.stdin.readline().rstrip().split()))

        for j in range(SIZE):
            if list_[j] >= max:
                max = list_[j]
                max_index[0] = i + 1
                max_index[1] = j + 1
    
    # 출력
    print(max)
    print(max_index[0], max_index[1])

if __name__ == "__main__":
    main()