def main():
    N = int(input())

    paper = []
    for i in range(N):
        inputData = list(map(int, input().split()))
        paper.append(inputData)

    print(paper)

if __name__ == "__main__":
    main()