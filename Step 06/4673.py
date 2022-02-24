def d(num):
    Hansu = num

    while num >= 1:
        Hansu += num % 10
        num = int(num / 10)
    return Hansu

def main():
    self_num = []
    for i in range(0, 10000+1):
        Hansu = d(i)
        if Hansu <= 10000 and Hansu not in self_num:
            self_num.append(Hansu)
    for i in range(0, 10000+1):
        if not i in self_num:
            print(i)

if __name__ == "__main__":
    main()