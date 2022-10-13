import os
def clear(): return os.system('cls')

# SOURCE_PATH = ""

# def log_out():
#     with open(SOURCE_PATH, 'w') as source: 
#         for line in f:
#             try:
#                 result *= mylist[int(line.strip())-1]
#             except ValueError:
#                 print("В файле содержится неправильное значение")
#                 return -1
#     return 0

def num_input():
    while True:
        try:
            imag = float(input("Введите мнимую часть: "))
            break
        except ValueError:
            print("Неверный ввод. Попробуйте ещё раз.")
    while True:
        try:
            real = float(input("Введите вещественную часть: "))
            break
        except ValueError:
            print("Неверный ввод. Попробуйте ещё раз.")

    return [real, imag]

def calc(operation, op1, op2):
    c1 = complex(op1[0],op1[1])
    c2 = complex(op2[0],op2[1])
    
    if operation == 1:
        res = c1+c2
    elif operation == 2:
        res = c1-c2
    elif operation == 3:
        res = c1*c2
    else:
        res = c1/c2
    return [res.real,res.imag]
    
    
def menu():
    
    operation = 0

    print("ПРОГРАММА - КАЛЬКУЛЯТОР\n")
    print("1. Сложение чисел")
    print("2. Вычитание чисел")
    print("3. Умножение чисел")
    print("4. Деление чисел\n")
    print("9. Лог событий\n")
    print("0. Выход\n")

    while True:
        try:
            point = int(input("Введите номер пункта меню: "))
            if point in [1,2,3,4,9,0]:
                break
        except ValueError:
            print("Введён неправильный пункт меню. Попробуйте ещё раз.")
    
    if point in [1,2,3,4]:
        operation = point
    elif point == 9:
        log_out()
        return
    else:
        exit()

    operand1 = num_input()
    operand2 = num_input()

    print(calc(operation, operand1, operand2))

    return


while True:    
    menu()
