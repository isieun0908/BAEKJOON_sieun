def main():
    n = int(input())

    stack = []
    pop = []
    for i in range(n):
        inputN = int(input())

        if len(stack)==0:
            for j in range(1, inputN+1):
                if not j in pop:
                    stack.append(j)
                    print("+")
            pop.append(stack.pop())
            print("-")
            continue
        lastNumber = stack[len(stack)-1]
        if inputN == lastNumber:
            pop.append(stack.pop())
            print("-")
        elif inputN < lastNumber:
            print("NO")
            break
        else:
            for j in range(lastNumber+1, inputN+1):
                if not j in pop:
                    stack.append(j)
                    print("+")
            pop.append(stack.pop())
            print("-")

if __name__ == "__main__":
    main()