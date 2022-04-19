def main():
    N = int(input())

    member = []
    for i in range(0, N):
        age, name = input().split()

        flag = 1
        for j in range(0, len(member)):
            if member[j][0] > age:
                member.insert(j, [age, name])
                flag = 0
                break
        if flag:
            member.append([age, name])

    for i in range(0, N):
        print(member[i][0], member[i][1])

if __name__ == "__main__":
    main()