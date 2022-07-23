def find_rectangle(N, paper):
    count = 0
    for pi in paper:
        for pj in pi:
            count += pj
    if count == 0:
        return 0
    elif count == N*N:
        return 1
    else:
        return -1

def cut(N, paper):
    if N == 1:
        if paper[0][0] == 0:
            print(0, end='')
            return
        elif paper[0][0] == 1:
            print(1, end='')
            return
    isRectangle = find_rectangle(N, paper)
    if isRectangle == 0:
        print(0, end='')
        return
    elif isRectangle == 1:
        print(1, end='')
        return
    else:
        print("(", end='')
        half_length = int(N/2)
        list_1 = []
        list_2 = []
        list_3 = []
        list_4 = []
        for i in range(0, half_length):
            list_1.append(paper[i][0:half_length])
            list_2.append(paper[i][half_length:N])
        for i in range(half_length, N):
            list_3.append(paper[i][0:half_length])
            list_4.append(paper[i][half_length:N])
        cut(half_length, list_1)
        cut(half_length, list_2)
        cut(half_length, list_3)
        cut(half_length, list_4)
        print(")", end='')

def main():
    N = int(input())

    image = []
    for i in range(N):
        inputData = input()
        line = []
        for num in inputData:
            line.append(int(num))
        image.append(line)
    cut(N, image)


if __name__ == "__main__":
    main()