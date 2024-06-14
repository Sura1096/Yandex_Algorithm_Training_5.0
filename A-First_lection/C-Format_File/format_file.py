'''
Петя - начинающий программист. Сегодня он написал код из n строк.
К сожалению оказалось, что этот код трудно читать. Петя решил исправить это, добавив в различные места пробелы.
А точнее, для i-й строки ему нужно добавить ровно ai пробелов.
Для добавления пробелов Петя выделяет строку и нажимает на одну из трёх клавиш: Space, Tab, и Backspace.
При нажатии на Space в строку добавляется один пробел. При нажатии на Tab в строку добавляются четыре пробела.
При нажатии на Backspace в строке удаляется один пробел.
Ему хочется узнать, какое наименьшее количество клавиш придётся нажать,
чтобы добавить необходимое количество пробелов в каждую строку. Помогите ему!

Формат ввода
Первая строка входных данных содержит одно целое положительное число n(1≤n≤105) – количество строк в файле.
Каждая из следующих n строк содержит одно целое неотрицательное число ai(0≤ai≤109) – количество пробелов,
которые нужно добавить в i-ю строку файла.

Формат вывода
Выведите одно число – минимальное количество нажатий, чтобы добавить в каждой строке необходимое количество пробелов.
'''


# def file_formatting(lines) -> int:
#     counter = 0
#
#     for i in range(lines):
#         el = int(input())
#         if el < 4:
#             if el > 1 + 4 - el:
#                 counter += 1 + 4 - el
#             else:
#                 counter += el
#         elif el >= 4 and el % 4 == 0:
#             counter += el // 4
#         else:
#             tab_space = (el // 4 + (el - (el // 4 * 4)))
#             tab_back = (el // 4 + 1 + abs(el - ((el // 4 + 1) * 4)))
#             if el >= tab_space >= tab_back:
#                 counter += tab_back
#             elif el >= tab_back >= tab_space:
#                 counter += tab_space
#             else:
#                 counter += el
#
#     return counter
#
#
# if __name__ == '__main__':
#     amount = int(input())
#     print(file_formatting(amount))


def file_formatting(lines):
    counter = 0

    for _ in range(lines):
        el = int(input())
        if el < 4:
            counter += min(el, 1 + 4 - el)
        elif el % 4 == 0:
            counter += el // 4
        else:
            tab_space = el // 4 + el % 4
            tab_back = el // 4 + 1 + abs(el - ((el // 4 + 1) * 4))
            counter += min(el, min(tab_space, tab_back))

    return counter


if __name__ == '__main__':
    amount = int(input())
    print(file_formatting(amount))