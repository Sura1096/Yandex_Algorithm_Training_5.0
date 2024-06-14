'''
k друзей организовали стартап по производству укулеле для кошек. На сегодняшний день прибыль составила n рублей.
Вы, как главный бухгалтер компании, хотите в каждый из ближайших d дней приписывать по одной цифре в конец числа,
выражающего прибыль. При этом в каждый из дней прибыль должна делиться на k.

Формат ввода
В единственной строке входных данных через пробел записаны три числа: n,k,d — изначальная прибыль,
количество учредителей компании и количество дней, которое вы собираетесь следить за прибылью (1≤n,k≤10^9,1≤d≤10^5).
НЕ гарантируется, что n делится на k.

Формат вывода
Выведите одно целое число x — прибыль компании через d дней. Первые цифры числа x должны совпадать с числом n.
Все префиксы числа x, которые длиннее числа n на 1,2,…,d цифр, должны делиться на k.
Если возможных ответов несколько, выведите любой из них. Если ответа не существует, выведите −1.
'''


def is_profit_of_d(n, k, d):
    res = str(n)
    for i in range(10):
        if int(res + str(i)) % k == 0:
            res += str(i)
            break
    if int(res) == n:
        return -1
    else:
        return res + ('0' * (d - 1))


if __name__ == '__main__':
    n, k, d = map(int, input().split())
    print(is_profit_of_d(n, k, d))