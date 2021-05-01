from typing import Literal


class MaxHeap:

    def __init__(self):
        self.heap = []
    
    def parent(self,i):
        if i == 0:
            return 0
        return (i-1)//2

    def size_heap(self):
        return len(self.heap)

    def isEmpty(self):
        return len(self.heap) == 0

    def swap_up(self, i):
        if (self.heap[self.parent(i)] < self.heap[i]):
            temp  = self.heap[self.parent(i)]
            self.heap[self.parent(i)] = self.heap[i]
            self.heap[i] = temp
            self.swap_up(self.parent(i))
        return True

    def push(self, value):
        self.heap.append(value)
        index = self.size_heap() - 1
        self.swap_up(index)


max_heap = MaxHeap()

max_heap.push(3)
max_heap.push(5)
max_heap.push(4)
max_heap.push(24)

print(max_heap.heap)



    