ef main():
    N = int(input())

    dungchi = []
    for i in range(0, N):
        w, h = map(int, input().split())
        dungchi.append([])
        dungchi[i].append(w)
        dungchi[i].append(h)

    for i in range(0, N):
        count = 1
        for j in range(0, N):
            if dungchi[i][0] < dungchi[j][0] and dungchi[i][1] < dungchi[j][1]:
                count += 1
        print(count, end=' ')

if __name__ == "__main__":
    main()