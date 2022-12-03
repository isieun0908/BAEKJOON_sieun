import sys
FULL_SIZE = 100
PART_SIZE = 10

def coloredPaper(full_paper, x, y):
    for i in range(x, x+PART_SIZE):
        for j in range(y, y+PART_SIZE):
            full_paper[i][j] = 1
    return full_paper

def checkColored(full_paper):
    colored = 0
    for i in range(FULL_SIZE):
        for j in range(FULL_SIZE):
            if full_paper[i][j] == 1:
                colored += 1
    return colored

def main():
    n = int(sys.stdin.readline().rstrip())
    full_paper = [ [ 0 for i in range(FULL_SIZE) ] for j in range(FULL_SIZE) ]
    for i in range(n):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        
        full_paper = coloredPaper(full_paper, x, y)
    
    colored = checkColored(full_paper)
    
    print(colored)


if __name__ == "__main__":
    main()