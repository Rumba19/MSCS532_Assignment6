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

def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    sublists = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    median_of_median = median_of_medians(medians, len(medians) // 2)
    less = [x for x in arr if x < median_of_median]
    equal = [x for x in arr if x == median_of_median]
    greater = [x for x in arr if x > median_of_median]
    if k < len(less):
        return median_of_medians(less, k)
    elif k < len(less) + len(equal):
        return median_of_median
    else:
        return median_of_medians(greater, k - len(less) - len(equal))
    


class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    def peek(self):
        return self.stack[-1] if not self.is_empty() else None
    def is_empty(self):
        return len(self.stack) == 0


if __name__ == "__main__":
    arr = [31, 7, 19, 3, 8, 4, 8, 9, 3]
    k = 3
    print(f"{k}th smallest element (Randomized Select):", randomized_select(arr[:], 0, len(arr)-1, k-1))
    print(f"{k}th smallest element (Median of Medians):", median_of_medians(arr[:], k-1))


#Output for stack
    stack = Stack()
    stack.push(33)
    stack.push(30)
    print("Stack Pop:", stack.pop())