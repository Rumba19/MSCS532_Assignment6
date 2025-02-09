import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_select(arr, low, high, k):
    if low == high:
        return arr[low]
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    p = partition(arr, low, high)
    if k == p:
        return arr[p]
    elif k < p:
        return randomized_select(arr, low, p - 1, k)
    else:
        return randomized_select(arr, p + 1, high, k)


if __name__ == "__main__":
    arr = [31, 7, 19, 3, 8, 4, 8, 9, 3]
    k = 3
    print(f"{k}th smallest element (Randomized Select):", randomized_select(arr[:], 0, len(arr)-1, k-1))
 
