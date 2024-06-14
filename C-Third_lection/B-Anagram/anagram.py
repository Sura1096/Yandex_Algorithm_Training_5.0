def is_anagram(first_word, second_word):
    if len(first_word) != len(second_word):
        return 'NO'

    first_word_dictionary = {}
    for el in first_word:
        first_word_dictionary[el] = first_word_dictionary.get(el, 0) + 1

    second_word_dictionary = {}
    for el in second_word:
        second_word_dictionary[el] = second_word_dictionary.get(el, 0) + 1

    for word_char, count in first_word_dictionary.items():
        if word_char not in second_word_dictionary:
            return 'NO'
        if word_char in second_word_dictionary and count != second_word_dictionary[word_char]:
            return 'NO'

    return 'YES'


if __name__ == '__main__':
    first = input()
    second = input()
    print(is_anagram(first_word=first, second_word=second))