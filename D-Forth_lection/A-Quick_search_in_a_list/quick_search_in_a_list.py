def left_bin_search(seq, target):
    left, right = 0, len(seq)
    while left < right:
        mid = left + (right - left) // 2
        if seq[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def right_bin_search(seq, target):
    left, right = 0, len(seq)
    while left < right:
        mid = left + (right - left) // 2
        if seq[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


def count_numbers_in_range(arr, left, right):
    left_index = left_bin_search(arr, left)
    right_index = right_bin_search(arr, right)
    return right_index - left_index


N = int(input())
numbers = list(map(int, input().split()))
K = int(input())
numbers.sort()
ans = []
for itt in range(K):
    L, R = map(int, input().split())
    count = count_numbers_in_range(numbers, L, R)
    ans.append(count)

print(*ans)
