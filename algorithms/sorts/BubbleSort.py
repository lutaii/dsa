def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if (arr[j + 1] < arr[j]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

print(bubble_sort([0,6,1,3,1,7,6,9,2]))