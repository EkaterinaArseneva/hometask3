""""Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

numbers = []
while True:
    line = input('enter numbers for summarizing, for exit type "q": ')
    numbers.extend(line.split())
    if "q" in numbers: #не хотела запускать for для проверки каждого символа в списке на "q". Но в моем решении я тогда
        # не знаю как сделать проверку на Q (т.к. некуда сделать upper. Или как то все таки можно?
        subtotal = sum(list(map(int, numbers[:numbers.index('q')])))
        print(f'subtotal is: {subtotal}')
        break
    else:
        subtotal = sum(list(map(int, numbers)))
    print(f'subtotal is: {subtotal}')
