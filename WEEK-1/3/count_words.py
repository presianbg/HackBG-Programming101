#!/usr/bin/python3


def count_words(arr):
    words = {}
    for word in arr:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words

if __name__ == '__main__':
    arr = ["python", "python", "python", "ruby"]
    print(count_words(arr))
