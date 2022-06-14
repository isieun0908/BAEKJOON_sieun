def main():
    stack = []
    while True:
        flag = 1
        stack.clear()
        inputData = input()
        if inputData == ".":
            break
        for i in inputData:
            if i == "(" or i == "[":
                stack.append(i)
            elif i == ")" or i == "]":
                if len(stack) > 0:
                    popData = stack.pop()
                    if not (popData == "(" and i == ")") and not (popData == "[" and i == "]"):
                        flag = 0
                        break
                else:
                    flag = 0
                    break
        if flag == 1:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()