import cmath
def main():
    x = complex(input().strip())
    print(abs(x))
    print(cmath.phase(x))

if __name__ == "__main__":
    main()