import numpy as np
import pandas as pd
import flask


def mergeSort(array):
    if len(array) == 1:
        return array
    mid = len(array)//2
    arr1 = mergeSort(array[:mid])
    arr2 = mergeSort(array[mid:])
    return merge(arr1, arr2)


def merge(a, b):
    i = j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1
    return c
