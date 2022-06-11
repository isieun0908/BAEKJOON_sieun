def main():
    stackS = []
    stackB = []
    while True:
        flag = 1
        stackS.clear()
        stackB.clear()
        inputData = input()
        if inputData == ".":
            break
        for i in inputData:
            if i == "(":
                stackS.append(1)
            elif i == "[":
                stackB.append(1)
            elif i == ")":
                if not len(stackS) == 0:
                    stackS.pop()
                else:
                    flag = 0
                    break
            elif i == "]":
                if not len(stackB) == 0:
                    stackB.pop()
                else:
                    flag = 0
                    break
        print(flag)
        if flag == 1:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()