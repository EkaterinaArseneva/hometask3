"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_func(num1, num2, num3):
    result = sum([num1, num2, num3]) - min(num1, num2, num3)
    return result


try:
    print(my_func(int(input('num1: ')), int(input('num2: ')), int(input('num3: '))))
except ValueError:
    print('ensure you enter numbers')
