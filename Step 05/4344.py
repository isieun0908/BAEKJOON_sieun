import sys

test_case = int(sys.stdin.readline())

for i in range(test_case):
    student = list(map(int, sys.stdin.readline().split()))
    num = student[0]
    del student[0]
    average = sum(student)/num

    count = 0
    for j in range(num):
        if student[j] > average:
            count += 1
    print("{:.3f}%".format(count/num*100))
