def main():
    T = int(input())

    for testCase in range(1, T+1):
        queue = []
        printNum = 0
        N, M = map(int, input().split())
        priority = list(map(int, input().split()))

        for i in range(0, N):
            queue.append([i, int(priority[i])])
        print(queue)

        while len(queue) > 0:
            item = queue.pop(0)
            flag = 0
            for i in queue:
                if queue[i][1] > 1:
                    flag = 1
                    break
            if flag:
                queue.append(item)
            else:
                printNum += 1
                if item[0] == M:
                    print(printNum)
                    break



if __name__ == "__main__":
    main()