from typing import List

def solution(lst):
    print('Input: ', lst)
    if len(lst) == 0:
        return []
    print('Output: ', mergeSort(0, len(lst) - 1, lst))

def mergeSort(l, r, lst):
    if l == r:
        return [lst[l]]
    m = l + (r - l) // 2
    left = mergeSort(l, m, lst)
    right = mergeSort(m + 1, r, lst)
    return merge(left, right)

def merge(left, right):
    res = []
    i, j = 0, 0
    while i != len(left) or j != len(right):
        if i == len(left):
            res.append(right[j])
            j += 1
        elif j == len(right):
            res.append(left[i])
            i += 1
        elif left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res

solution([4, 5, 3, 6, 4, 7, 11, 16, 4, 1])