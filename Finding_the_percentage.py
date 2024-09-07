def main():
    number_inputs = int(input().strip())
    student_marks = {}
    for _ in range(number_inputs):
        # * is used to take input as a list
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input().strip()
    print(
        "{:.2f}".format(
            sum(student_marks[query_name]) / student_marks[query_name].__len__()
        )
    )


if __name__ == "__main__":
    main()
