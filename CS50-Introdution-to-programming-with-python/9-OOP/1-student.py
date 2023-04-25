def main():
    name = get_name()
    house = get_house()
    print(f'{name} from {house}')


def get_name(): 
    return input('What is your name? ')


def get_house():
    return input('What house do you belong to? ')


if __name__ == '__main__':
    main()