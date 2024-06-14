def is_repeat(k, numbers):
    nums_dict = {}
    for ind, num in enumerate(numbers):
        if num not in nums_dict:
            nums_dict[num] = ind
        else:
            if ind - nums_dict[num] <= k:
                return 'YES'
            else:
                nums_dict[num] = ind
    return 'NO'


if __name__ == '__main__':
    number_amount, distance = map(int, input().split())
    nums_list = list(map(int, input().split()))
    print(is_repeat(distance, nums_list))