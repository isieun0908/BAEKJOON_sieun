def push(x, stack):
    stack.append(x)

def empty(stack):
    if len(stack) == 0:
        return 1
    else:
        return 0

def main():
    N = int(input())
    stack = []

    for i in range(N):
        inputData = input()

        try:
            command = inputData.split()

            if command[0] == "push":
                push(command[1], stack)
        except:
            if inputData == "empty":
                print(empty(stack))
            elif inputData == "size":
                print(len(stack))
            elif inputData == "front":
                if empty(stack) == 1:
                    print(-1)
                else:
                    print(stack[0])
            elif inputData == "back":
                if empty(stack) == 1:
                    print(-1)
                else:
                    print(stack[len(stack)-1])
            elif inputData == "pop":
                if empty(stack) == 1:
                    print(-1)
                else:
                    print(stack.pop(0))

if __name__ == "__main__":
    main()