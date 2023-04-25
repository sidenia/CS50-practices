def main():
    student = get_student()
    print(f'{student[0]} from {student[1]}')


def get_student():
    name = input('Enter name: ')
    house = input('Enter house: ')
    return name, house

if __name__ == '__main__':
    main()