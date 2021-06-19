import numpy as np
import pandas as pd
import flask


def mergeSort(array):
    if len(array) == 1:
        return array
    mid = len(array)//2
    print(array[:mid], array[mid:], "hello")
    arr1 = mergeSort(array[:mid])
    print(arr1)
    arr2 = mergeSort(array[mid:])
    print(arr2)
    return merge(arr1, arr2)


def merge(a, b):
    # print(a, b, "hello")
    i = j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
        # print(c)
    while i < len(a):
        c.append(a[i])
        i += 1
        # print(c)
    while j < len(b):
        c.append(b[j])
        j += 1
        # print(c)
    return c


# N = int(input())

# arr = list()
# for _ in range(N):

#     arr.append(int(input()))

print(mergeSort([7, 5, 1, 6, 9, 12]))
