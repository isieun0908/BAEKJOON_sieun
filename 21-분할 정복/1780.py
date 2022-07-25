def all_equal(paper):
    first_item = paper[0][0]

    for line in paper:
        for item in line:
            if not first_item == item:
                return -100
    return first_item

def cut(paper):
    if len(paper) == 1:
        if paper[0][0] == 1:
            return [0, 0, 1]
        elif paper[0][0] == 0:
            return [0, 1, 0]
        elif paper[0][0] == -1:
            return [1, 0, 0]
    isAllEqual = all_equal(paper)
    if isAllEqual == 1:
        return [0, 0, 1]
    elif isAllEqual == 0:
        return [0, 1, 0]
    elif isAllEqual == -1:
        return [1, 0, 0]

    result = [0, 0, 0]

    cut_size = int(len(paper) / 3)
    cut_1 = []
    cut_2 = []
    cut_3 = []
    for i in range(len(paper)):
        cut_1.append(paper[i][0:cut_size])
        cut_2.append(paper[i][cut_size:cut_size*2])
        cut_3.append(paper[i][cut_size*2:len(paper)])

        if len(cut_1) == len(paper) // 3:
            result_1 = cut(cut_1)
            result_2 = cut(cut_2)
            result_3 = cut(cut_3)

            for i in range(3):
                result[i] += result_1[i] + result_2[i] + result_3[i]
            cut_1 = []
            cut_2 = []
            cut_3 = []
    return result

def main():
    N = int(input())

    paper = []
    for i in range(N):
        inputLine = list(map(int, input().split()))
        paper.append(inputLine)

    result = cut(paper)
    for r in result:
        print(r)

if __name__ == "__main__":
    main()