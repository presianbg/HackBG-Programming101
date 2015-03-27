#!/usr/bin/python3


def group(items):
    big_list = []
    small_list = []
    for index in range(len(items) - 1):
        if items[index] == items[index+1]:
            small_list.append(items[index])
        elif items[index] == items[index-1]:
            small_list.append(items[index])
            big_list.append(small_list)
            small_list = []
        else:
            small_list.append(items[index])
            big_list.append(small_list)
            small_list = []
    if items[len(items)-1] == items[len(items)-2]:
        small_list.append(items[index])
        big_list.append(small_list)
        small_list = []
    else:
        small_list.append(items[len(items)-1])
        big_list.append(small_list)
        small_list = []
    return big_list


if __name__ == '__main__':
    items = [1, 1, 1, 2, 3, 1, 3, 3, 5, 3, 3]
    print(group(items))
