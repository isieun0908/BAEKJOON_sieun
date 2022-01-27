def main():
    inputS = input()

    sum = 0
    for i in range(0, len(inputS)):
        if inputS[i] == "A" or inputS[i] == "B" or inputS[i] == "C":
            sum += 3
        elif inputS[i] == "D" or inputS[i] == "E" or inputS[i] == "F":
            sum += 4
        elif inputS[i] == "G" or inputS[i] == "H" or inputS[i] == "I":
            sum += 5
        elif inputS[i] == "J" or inputS[i] == "K" or inputS[i] == "L":
            sum += 6
        elif inputS[i] == "M" or inputS[i] == "N" or inputS[i] == "O":
            sum += 7
        elif inputS[i] == "P" or inputS[i] == "Q" or inputS[i] == "R" or inputS[i] == "S":
            sum += 8
        elif inputS[i] == "T" or inputS[i] == "U" or inputS[i] == "V":
            sum += 9
        elif inputS[i] == "W" or inputS[i] == "X" or inputS[i] == "Y" or inputS[i] == "Z":
            sum += 10
    print(sum)
if __name__ == "__main__":
    main()