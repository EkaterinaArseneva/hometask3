"""Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


# opt1
# def my_exponentiation(num1, num2):
#     result = num1**num2 if type(num1) == float and type(num2) is int and num2 < 0 else 'try again, wrong parameters'
#     return result
# print(f'exponentiation result is: {my_exponentiation(float(input("num1: ")), (int(input("num2: "))))}')

# opt2

def my_exponentiation(num1, num2):
    if type(num1) == float and type(num2) is int and num2 < 0:
        div = 0
        for i in range(1, -num2):
            div += num1 * num1
        result = 1 / div
    else:
        result = 'try again, wrong parameters'
    return result


print(f'exponentiation is: {my_exponentiation(float(input("enter num1: ")), int(input("enter num2: ")))}')
