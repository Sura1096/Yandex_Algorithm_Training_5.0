def intersection_two_of_three(first_list, second_list, third_list):
    first_and_second = first_list & second_list
    first_and_third = first_list & third_list
    second_and_third = second_list & third_list

    union_set = list(first_and_second | first_and_third | second_and_third)

    union_set.sort()
    print(*union_set)


if __name__ == '__main__':
    first = int(input())
    list_1 = set(map(int, input().split()))

    second = int(input())
    list_2 = set(map(int, input().split()))

    third = int(input())
    list_3 = set(map(int, input().split()))

    intersection_two_of_three(list_1, list_2, list_3)