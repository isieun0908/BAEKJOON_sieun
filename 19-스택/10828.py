def main():
    N = int(input())
    stack = []

    for i in range(N):
        inputData = input()

        if inputData[0:4] == "push":
            push_command = inputData.split()
            stack.append(int(push_command[1]))
        else:
            if inputData == "pop":
                if len(stack) == 0:
                    result = -1
                else:
                    result = stack.pop()
            elif inputData == "size":
                result = len(stack)
            elif inputData == "empty":
                if len(stack) == 0:
                    result = 1
                else:
                    result = 0
            elif inputData == "top":
                if len(stack) == 0:
                    result = -1
                else:
                    result = stack[len(stack)-1]
            print(result)

if __name__ == "__main__":
    main()