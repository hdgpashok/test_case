from task_A import get_balance


def main():
    inn = input("Введите команду\n").split()

    if inn[0] == 'get_balance':
        print(get_balance(inn[1]))


if __name__ == '__main__':
    main()