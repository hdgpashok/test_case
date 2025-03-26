from task_A import get_balance
from task_B import get_balance_batch

def main():
    inn = input("Введите команду\n").split()

    if inn[0] == 'get_balance':
        print(get_balance(inn[1]))

    elif inn[0] == "get_balance_batch":
        print("Вставьте кошельки в файл wallets.txt")
        print(get_balance_batch())

if __name__ == '__main__':
    main()