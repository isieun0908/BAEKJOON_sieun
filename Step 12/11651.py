def main():
    N = int(input())
    list = []
    for i in range(0, N):
        x, y = map(int, input().split())
        list.append([y, x])
    list.sort()

    for i in range(0, N):
        print(list[i][1], list[i][0])

if __name__ == "__main__":
    main()