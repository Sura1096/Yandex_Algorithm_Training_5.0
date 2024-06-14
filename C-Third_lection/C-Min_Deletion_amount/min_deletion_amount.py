def min_deletion_amount(amount, nums):
    if amount <= 0:
        raise ValueError('Amount of list elements should be greater than or equal to 1')
    elif amount > 2 * (10**5):
        raise ValueError('Amount of list elements should be less than or equal to 2 * 10^5')

    nums_dict = {}
    for num in nums:
        nums_dict[num] = nums_dict.get(num, 0) + 1

    mini = float('inf')
    for num in nums_dict.keys():
        mini = min(mini, amount - nums_dict[num] - nums_dict.get(num+1, 0))

    return mini


if __name__ == '__main__':
    nums_amount = input()
    try:
        nums_amount = int(nums_amount)
        numbers_list = list(map(int, input().split()))
        print(min_deletion_amount(nums_amount, numbers_list))
    except ValueError:
        print('Input value must be integer.')