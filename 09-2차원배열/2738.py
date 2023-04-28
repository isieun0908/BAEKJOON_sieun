import sys

def main():
    # 2차원 배열 크기 입력
    n, m = map(int, sys.stdin.readline().rstrip().split())

    # 첫 번째 2차원 배열 입력
    list_1 = []
    for i in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        list_1.append(line)
    
    # 두 번째 2차원 배열 입력
    list_2 = []
    for i in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        list_2.append(line)

    # 두 2차원 배열 합
    new_list = [[0 for col in range(m)] for row in range(n)]

    for i in range(0, n):
        for j in range(0, m):
            new_list[i][j] = list_1[i][j] + list_2[i][j]
            print(new_list[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()