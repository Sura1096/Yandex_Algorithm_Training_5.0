from random import randint


'''
Раунд плей-офф между двумя командами состоит из двух матчей.
Каждая команда проводит по одному матчу «дома» и «в гостях». Выигрывает команда, забившая большее число мячей.
Если же число забитых мячей совпадает, выигрывает команд, забившая больше мячей «в гостях». Если и это число мячей совпадает, матч переходит в дополнительный тайм или серию пенальти.

Вам дан счёт первого матча, а также счёт текущей игры (которая ещё не завершилась). Помогите комментатору сообщить,
сколько голов необходимо забить первой команде, чтобы победить, не переводя игру в дополнительное время.

Формат ввода
В первой строке записан счёт первого мачта в формате G1:G2, где G1 "— число мячей, забитых первой командой,
а G2 "— число мячей, забитых второй командой.
Во второй строке записан счёт второго (текущего) матча в аналогичном формате. Все числа в записи счёта не превышают 5.
В третьей строке записано число 1, если первую игру первая команда провела «дома», или 2, если «в гостях».

Формат вывода
Выведите единственное целое число "— необходимое количество мячей.
'''


def ball_amount(g1_first: int, g2_first: int, g1_second: int, g2_second: int, game: int) -> int:
    sum1 = g1_first + g1_second
    sum2 = g2_first + g2_second
    result = sum2 - sum1

    if sum1 <= sum2 and game == 1:
        if result + g1_second <= g2_first:
            result += 1
    elif sum1 <= sum2 and game == 2:
        if g1_first <= g2_second:
            result += 1
    else:
        return 0

    return result


if __name__ == '__main__':
    # g1_first, g2_first = map(int, input().split(':'))
    # g1_second, g2_second = map(int, input().split(':'))
    # game = int(input())
    # print(ball_amount(g1_first, g2_first, g1_second, g2_second, game))

    iteration = 10
    while iteration > 0:
        g1_first = randint(0, 5)
        g2_first = randint(0, 5)

        g1_second = randint(0, 5)
        g2_second = randint(0, 5)

        game = randint(1, 2)
        print(f'{g1_first}, {g2_first}, {g1_second}, {g2_second}, {game}')
        print(ball_amount(g1_first, g2_first, g1_second, g2_second, game))
        print()
        iteration -= 1