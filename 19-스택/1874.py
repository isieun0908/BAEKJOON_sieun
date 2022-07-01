def main():
    n = int(input())

    stack = []
    for i in range(n):
        inputN = int(input())

        if len(stack) == 0:
            stack.append(inputN)
            continue
        for j in range(0, len(stack)):
            if stack[j] < inputN:
                print("<<")

if __name__ == "__main__":
    main()