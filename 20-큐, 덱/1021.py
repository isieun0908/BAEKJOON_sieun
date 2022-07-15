def main():
    N, M = map(int, input().split())
    location = list(map(int, input().split()))

    queue = []
    for i in range(1, N+1):
        queue.append(i)

    count = 0
    get_count = 0
    while True:
        if queue[0] == location[get_count]:
            queue.pop(0)
            get_count += 1
        elif queue.index(location[get_count]) <= len(queue)-queue.index(location[get_count]):
            num = queue.pop(0)
            queue.append(num)
            count += 1
        else:
            num = queue.pop()
            queue.insert(0, num)
            count += 1

        if get_count >= M:
            break
    print(count)


if __name__ == "__main__":
    main()