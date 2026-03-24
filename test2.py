import random


def generate_random_list(n, min, max):

    l = []
    for i in range(n):
        l.append(random.randint(min, max))
    return l


def select_sort(l: list) -> list:

    for index in range(len(l)):

        unsorted_index = index
        min_number = l[unsorted_index]
        min_index = unsorted_index

        for i in range(unsorted_index, len(l)):
            if l[i] < min_number:
                min_number = l[i]
                min_index = i
        l[min_index] = l[unsorted_index]
        l[unsorted_index] = min_number

    return l


def buble_sort(l: list) -> list:
    for index in range(len(l)):
        unsorted_index = 0
        for i in range(unsorted_index, len(l) - 1):
            if l[i + 1] < l[i]:
                min_number = l[i + 1]
                l[i + 1] = l[i]
                l[i] = min_number
    return l


# l = generate_random_list(10, 0, 500)
l = generate_random_list(10, -50, 50)
print(l)
print(select_sort(l))
print(buble_sort(l))
