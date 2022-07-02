def main():
    n = int(input())

    stack = []
    for i in range(n):
        inputN = int(input())

        if len(stack) == 0:
            stack.append(inputN)
            print("+")
            continue

        temp = []
        for j in range(len(stack)-1, -1, -1):
            if stack[j] > inputN:
                temp.insert(0, stack.pop())
                print("-")
            else:
                break
        stack.append(inputN)
        print("+")
        stack += temp

if __name__ == "__main__":
    main()