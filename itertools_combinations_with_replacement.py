from itertools import combinations_with_replacement


def main():
    string, n = input().split()
    n = int(n)
    comb = combinations_with_replacement(sorted(string), n)
    for i in list(comb):
        print("".join(i))


if __name__ == "__main__":
    main()
