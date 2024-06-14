def min_segments(a):
    cur_size = a[0]
    segments_length = []
    segment_size = 0

    for el in a:
        if el < cur_size:
            cur_size = el
        if segment_size < cur_size:
            segment_size += 1
        else:
            segments_length.append(segment_size)
            cur_size = el
            segment_size = 1
    segments_length.append(segment_size)

    print(len(segments_length))
    print(*segments_length)


if __name__ == '__main__':
    t = int(input())
    for itt in range(t):
        n = int(input())
        lst = list(map(int, input().split()))
        min_segments(lst)