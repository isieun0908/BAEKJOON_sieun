def checkEmpty(stack):
    if len(stack) == 0:
        return 1
    else:
        return 0

def main():
    T = int(input())

    stack = []
    for i in range(T):
        stack.clear()
        flag = 0
        inputData = input()
        for w in inputData:
            if w == "(":
                stack.append(w)
            else:
                if checkEmpty(stack) == 0:
                    stack.pop()
                else:
                    flag = 1
                    break
        if checkEmpty(stack) == 1 and flag == 0:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()