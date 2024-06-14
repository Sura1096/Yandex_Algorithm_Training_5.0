def min_square(coordinates_list: list) -> str:
    if len(coordinates_list) == 1:
        return f'{coordinates_list[0][0]} {coordinates_list[0][1]} {coordinates_list[0][0]} {coordinates_list[0][1]}'

    min1 = min(coordinates_list[0][0], coordinates_list[1][0])
    max1 = max(coordinates_list[0][0], coordinates_list[1][0])

    min2 = min(coordinates_list[0][1], coordinates_list[1][1])
    max2 = max(coordinates_list[0][1], coordinates_list[1][1])

    for el in coordinates_list:
        min1 = min(min1, el[0])
        max1 = max(max1, el[0])

        min2 = min(min2, el[1])
        max2 = max(max2, el[1])

    return f'{min1} {min2} {max1} {max2}'


if __name__ == '__main__':
    K = int(input())
    coordinates = []
    for i in range(K):
        x, y = map(int, input().split())
        coordinates.append([x, y])

    print(min_square(coordinates))