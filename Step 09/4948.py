def main():
    while True:
        inputNum = int(input())
        if inputNum == 0:
            break

        prime = []
        prime.append(1)
        for i in range(2, 2*inputNum+1):
            loop = 2
            while i * loop <= 2*inputNum+1:
                if not i*loop in prime:
                    prime.append(i * loop)
                loop += 1

        count = 0
        for i in range(inputNum+1, 2*inputNum+1):
            if not i in prime:
                count += 1
        print(count)

if __name__ == "__main__":
    main()