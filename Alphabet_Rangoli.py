alphabets = "abcdefghijklmnopqrstuvwxyz"


def print_rangoli(size):
    parts_of_rangoli = []
    for index in range(size):
        temp = "-".join(alphabets[index:size])
        parts_of_rangoli.append(temp[::-1] + temp[1:])
    for line in range(size - 1, 0, -1):
        print(parts_of_rangoli[line].center(size * 4 - 3, "-"))
    for line in parts_of_rangoli:
        print(line.center(size * 4 - 3, "-"))


if __name__ == "__main__":
    size = int(input())
    print_rangoli(size)
