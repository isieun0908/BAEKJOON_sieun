def main():
    K = int(input())

    stack = []
    for i in range(K):
        inputData = int(input())
        if inputData == 0:
            stack.pop()
        else:
            stack.append(inputData)
    print(sum(stack))

if __name__ == "__main__":
    main()