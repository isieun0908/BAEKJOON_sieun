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
            return [1, 0]
        elif paper[0][0] == 1:
            return [0, 1]
    isRectangle = find_rectangle(N, paper)
    if isRectangle == 0:
        return [1, 0]
    elif isRectangle == 1:
        return [0, 1]
    else:
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
        result = [0, 0]
        list_1_result = cut(half_length, list_1)
        list_2_result = cut(half_length, list_2)
        list_3_result = cut(half_length, list_3)
        list_4_result = cut(half_length, list_4)
        result[0] = list_1_result[0] + list_2_result[0] + list_3_result[0] + list_4_result[0]
        result[1] = list_1_result[1] + list_2_result[1] + list_3_result[1] + list_4_result[1]
        return result

def main():
    N = int(input())

    paper = []
    for i in range(N):
        inputData = list(map(int, input().split()))
        paper.append(inputData)

    result = cut(N, paper)
    print(result[0])
    print(result[1])

if __name__ == "__main__":
    main()