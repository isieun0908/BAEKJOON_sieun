def main():
    N = int(input())
    list = []

    for i in range(0, N):
        x, y = map(int, input().split())
        list.append([x,y])
    list.sort()
    for i in range(0, N):
        print(list[i][0], list[i][1])

if __name__ == "__main__":
    main()