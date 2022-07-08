def main():
    N, K = map(int, input().split())

    circle = []
    for i in range(1, N+1):
        circle.append(i)
    index = K - 1
    while len(circle) > 1:
        print(circle.pop(index))
        index = (index+K-1) % len(circle)
    print(circle[0])

if __name__ == "__main__":
    main()