def bin_search(n):
    left = 1
    right = n
    k = 0

    while left <= right:
        mid = (left + right) // 2
        if check_condition(mid, n):
            k = mid
            left = mid + 1
        else:
            right = mid - 1
    return k


def check_condition(k, n):
    total_cells = (k * ((k**2) + (6 * k) + 5) - 1) // 6
    return total_cells <= n


n = int(input())
print(bin_search(n))


# 117055765888857794
# 973622521965965999