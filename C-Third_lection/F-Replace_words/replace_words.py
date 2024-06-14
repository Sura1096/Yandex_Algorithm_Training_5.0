def replaced_text(dictionary, words):
    for i, word in enumerate(words):
        for ind in range(len(word)):
            if word[:ind + 1] in dictionary:
                words[i] = word[:ind + 1]
                break

    return words


if __name__ == '__main__':
    dct = set(map(str, input().split()))
    txt = list(map(str, input().split()))
    print(*replaced_text(dct, txt))
