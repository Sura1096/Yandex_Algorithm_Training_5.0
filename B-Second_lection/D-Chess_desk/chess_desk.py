def perimeter(cells):
    '''
    Returns perimeter of the figure by its coordinates.
    '''

    result = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # up, down, right, left - directions

    for cell in cells:
        row, col = cell

        # Check whether current cell has neighbours in up, down, right, left directions
        for row_direction, column_direction in directions:
            new_row, new_col = row + row_direction, col + column_direction

            # if cell doesn't have neighbours, increment side, i.e. perimeter
            if (new_row, new_col) not in cells:
                result += 1

    return result


if __name__ == '__main__':
    N = int(input())
    coordinates = set()
    for i in range(N):
        x, y = map(int, input().split())
        coordinates.add((x, y))
    print(perimeter(coordinates))