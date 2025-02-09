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

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
    def delete(self, value):
        current = self.head
        prev = None
        while current and current.value != value:
            prev = current
            current = current.next
        if prev is None:
            self.head = current.next
        elif current:
            prev.next = current.next
    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
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

  #Output for Queue      
    queue = Queue()
    queue.enqueue(5) 
    queue.enqueue(7) 
    print("Queue Dequeue:", queue.dequeue())

    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.traverse()
    linked_list.delete(2)
    linked_list.traverse()