from itertools import permutations


def main():
    string, n = input().split()
    n = int(n)
    perm = permutations(string, n)
    perm = sorted(perm)
    for i in list(perm):
        print("".join(i))


if __name__ == "__main__":
    main()
