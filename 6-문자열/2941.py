def main():
    inputData = input()

    Count = 0
    for index in range(0, len(inputData)):
        if inputData[index]=="c":
            if index+1 != len(inputData) and inputData[index+1]=="=":
                index += 1
                Count -= 1
            elif index+1 != len(inputData) and inputData[index+1]=="-":
                index += 1
                Count -= 1
        elif inputData[index]=="d":
            if index+1 != len(inputData) and inputData[index+1]=="z" and index+2 != len(inputData) and inputData[index+2]=="=":
                index += 2
                Count -= 1
            elif index + 1 != len(inputData) and inputData[index + 1] == "-":
                index += 1
                Count -= 1
        elif inputData[index]=="l":
            if index+1 != len(inputData) and inputData[index+1]=="j":
                index += 1
                Count -= 1
        elif inputData[index]=="n":
            if index+1 != len(inputData) and inputData[index+1]=="j":
                index += 1
                Count -= 1
        elif inputData[index]=="s":
            if index+1 != len(inputData) and inputData[index+1]=="=":
                index += 1
                Count -= 1
        elif inputData[index]=="z":
            if index+1 != len(inputData) and inputData[index+1]=="=":
                index += 1
                Count -= 1
        Count += 1
    print(Count)

if __name__ =="__main__":
    main()