from collections import defaultdict


def main():
    size_of_a, size_of_b = map(int, input().split())
    dictionary_a = defaultdict(list)
    for i in range(size_of_a):
        dictionary_a[input().strip()].append(i + 1)
    queries = []
    for i in range(size_of_b):
        queries.append(input().strip())
    for i in queries:
        if i in dictionary_a:
            print(*dictionary_a[i])
        else:
            print(-1)


if __name__ == "__main__":
    main()
