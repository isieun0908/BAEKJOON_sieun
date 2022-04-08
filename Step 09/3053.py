import math

def main():
    r = int(input())

    euclid = "{:.6f}".format(r*r*math.pi)
    taxicab = "{:.6f}".format(float(2*r*r))
    print(euclid)
    print(taxicab)

if __name__ == "__main__":
    main()