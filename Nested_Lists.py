def main():
    student_number = int(input())
    student_marks = {}
    for _ in range(student_number):
        name = input()
        score = float(input().strip())
        if score not in student_marks:
            student_marks[score] = [name]
        else:
            student_marks[score].append(name)
    second_lowest = sorted(student_marks.keys())[1]
    student_marks[second_lowest].sort()
    print("\n".join(student_marks[second_lowest]))


if __name__ == "__main__":
    main()
