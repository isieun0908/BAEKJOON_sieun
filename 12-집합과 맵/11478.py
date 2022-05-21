def main():
    S = input()

    partString = {}
    for i in range(0, len(S)+1):
        for j in range(i+1, len(S)+1):
            partString[S[i:j]] = 0
    print(len(partString))

if __name__ == "__main__":
    main()