def main():
    TestCase = int(input())

    for testCase in range(0, TestCase):
        k = int(input())
        n = int(input())

        list = []
        list.append([])
        for i in range(0, n):
            list[0].append(i+1)
        for i in range(1, k+1):
            list.append([])
            for j in range(0, n):
                sum = 0
                for p in range(0, j+1):
                    sum += list[i-1][p]
                list[i].append(sum)
        print(list[len(list)-1][len(list[len(list)-1])-1])

if __name__ == "__main__":
    main()