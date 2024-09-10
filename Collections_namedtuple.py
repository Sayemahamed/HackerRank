from collections import namedtuple


def main():
    students = int(input())
    student = namedtuple("student", input().split())
    students_data = []
    for _ in range(students):
        students_data.append(student(*input().split()))
    print(sum(int(i.MARKS) for i in students_data) / students)


if __name__ == "__main__":
    main()
