from itertools import combinations


def main():
    s, n = input().split()
    n = int(n)
    for i in range(1, n + 1):
        for combo in combinations(sorted(s), i):
            print("".join(combo))


if __name__ == "__main__":
    main()
