def main():
    Word = input()
    alpha = {}
    max = 0
    for i in range(0, len(Word)):
        findWord = Word[i].upper()
        if findWord in alpha:
            alpha[findWord] += 1
        else:
            alpha[findWord] = 1
        if alpha[findWord] > max:
            max = alpha[findWord]
            maxAlpha = findWord
        elif alpha[findWord] == max:
            maxAlpha = '?'
    print(maxAlpha)

if __name__ == "__main__":
    main()