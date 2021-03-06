def push(x, stack):
    stack.append(x)
    return stack

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
                stack = push(command[1], stack)
            elif inputData == "empty":
                print(empty(stack))
            elif inputData == "size":
                print(len(stack))
            elif command[0] == "front":
                if empty(stack) == 1:
                    print(-1)
                else:
                    print(stack[0])
            elif inputData == "back":
                if empty(stack):
                    print(-1)
                else:
                    print(stack[len(stack)-1])
            elif inputData == "pop":
                if empty(stack) == 1:
                    print(-1)
                else:
                    print(stack.pop(0))
            else:
                print("else")
        except:
            print("except")

if __name__ == "__main__":
    main()