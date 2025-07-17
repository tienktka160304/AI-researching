def gradingStudents(grades):
    round = []
    for i in grades:
        next_multiple_number = ((i // 5) + 1) * 5
        if(i < 38):
            round.append(i)
        else:
            if((next_multiple_number - i) <3):
                round.append(next_multiple_number)
            else:
                round.append(i)
    return round

if __name__ == '__main__':
    grades_count = int(input())
    grades = []
    for _ in range(grades_count):
        grades.append(int(input()))
    result = gradingStudents(grades)
    print(result)
