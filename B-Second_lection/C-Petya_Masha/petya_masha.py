def min_length(n: int, l: list) -> int:
    maxi = 0
    ind = 0

    for i in range(n):
        if l[i] > maxi:
            maxi = l[i]
            ind = i

    summ_rest_nums = 0
    for i in range(n):
        if i != ind:
            summ_rest_nums += l[i]

    if maxi > summ_rest_nums:
        return maxi - summ_rest_nums
    return maxi + summ_rest_nums


if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    print(min_length(n, l))