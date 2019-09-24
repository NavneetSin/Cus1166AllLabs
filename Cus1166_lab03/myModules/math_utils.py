def average_grade(roster):
    sum = 0
    number_of_grades = 0
    for item in roster:
        sum += item.get_grade()
        number_of_grades += 1
    return sum / number_of_grades