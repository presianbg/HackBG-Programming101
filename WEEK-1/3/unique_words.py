#!/usr/bin/python3
from count_words import count_words


def unique_words_count(arr):
    words = count_words(arr)
    return len(words)


if __name__ == '__main__':
    arr = ["python", "python", "python", "ruby"]
    print(unique_words_count(arr))
