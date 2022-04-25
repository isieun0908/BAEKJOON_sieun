def main():
    num = int(input())

    count = 0
    gap = 0
    while num > gap:
        gap += count
        count += 1

    if count % 2 == 1:
        print(str(count-(gap-num+1))+"/"+str(gap-num+1))
    else:
        print(str(gap - num + 1)+"/"+str(count - (gap - num + 1)))

if __name__ == "__main__":
    main()