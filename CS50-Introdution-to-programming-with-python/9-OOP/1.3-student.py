def main():
    student = get_student()
    print(f'{student["name"]} from {student["school"]}')


def get_student():
    student = {}
    student['name'] = input('Enter student name: ')
    student['school'] = input('Enter student school: ')
    return student

if __name__ == '__main__':
    main()