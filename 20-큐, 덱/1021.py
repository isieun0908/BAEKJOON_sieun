def main():
    N, M = map(int, input().split())
    location = list(map(int, input().split()))

    queue = []
    for i in range(1, N+1):
        queue.append(i)

    count = 0
    for i in range(M):
        if queue[0] == location[i]:
            queue.pop(0)
        elif queue[0] < location[i]:
            num = queue.pop(0)
            queue.append(num)
            count += 1
        elif queue[0] > location[i]:
            num = queue.pop()
            queue.insert(num)
            count += 1
    print(count)


if __name__ == "__main__":
    main()