from itertools import groupby


def main():
    string = input()
    for k, g in groupby(string):
        print((len(list(g)), int(k)), end=" ")


if __name__ == "__main__":
    main()
