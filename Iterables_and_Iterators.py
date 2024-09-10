from itertools import combinations


def main():
    input()
    array = input().split()
    k = int(input())
    combinations_ = list(combinations(array, k))
    contains_a = [i for i in combinations_ if "a" in i]
    print(len(contains_a) / len(combinations_))


if __name__ == "__main__":
    main()
