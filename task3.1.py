"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""
#opt 1
# def division_func(num1, num2):
#     result = 'error: division by zero, try again' if num2 == 0 else (num1/num2)
#     return result
#
#
# print(f'division result is {division_func(int(input("enter 1st number: ")), int(input("enter 2nd number: ")))}')
#

#opt 2 - не хорошо, т.к. длинная строка, да?
print(f'division result is :{(lambda num1, num2: num1/num2 if num2 != 0 else "error: division by zero, try again") (int(input("enter 1st number: ")),int(input("enter 2nd number ")))}')
