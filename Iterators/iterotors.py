"""
Nested list live
"""
MAX_SCORE = 50
def get_aboved(students):
    """Print name of students who scored better than 75%"""
    the_best_students = []
    for students in students:
        name = students[0]
        score = students[1]
        score_percentage = score / MAX_SCORE * 100

        if score_percentage >= 75:
            the_best_students.append(students)
            print(name)

def get_second_score(students):
    sorted_students = sorted(students)
    print(sorted_students)


def main():
    students_list = [
        ['Sam', 40.5], ['Tom', 49.5], ['Steve', 40.5],
        ['John', 30.1], ['Arya', 32.2],
    ]
    #get_above(students_list)
    get_aboved(students_list)

if __name__ == '__main__':
    main()