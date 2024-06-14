def common_music(people_amount):
    music = set()

    for itt in range(people_amount):
        favorite_music_amount = int(input())
        favorite_music_names = list(map(str, input().split()))
        if itt != 0:
            music &= set(favorite_music_names)
        else:
            music = set(favorite_music_names)

    music = list(music)
    music.sort()

    print(len(music))
    print(*music)


if __name__ == '__main__':
    people_group_amount = int(input())
    common_music(people_group_amount)