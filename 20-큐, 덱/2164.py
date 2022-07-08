def main():
    N = int(input())

    queue = []

    for i in range(1, N+1):
        queue.append(i)
    while len(queue) > 1:
        queue.pop(0)
        moveCard = queue.pop(0)
        queue.append(moveCard)
    print(queue[0])

if __name__ == "__main__":
    main()