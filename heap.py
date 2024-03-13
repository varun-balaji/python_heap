import math
from typing import Optional

# Max heap
class Heap:
    def __init__(self, iter: Optional[list[int]] = None):
        self.heap = []
        if iter is None:
            return
        for i in iter:
            self.push(i)

    def push(self, elem: int):
        """Push element into heap in O(log(n)) time"""
        self.heap.append(elem)
        print("Pushed", elem)
        elem_index = len(self.heap) - 1
        parent_index = (elem_index - 1) // 2
        if parent_index < 0:
            return
        while self.heap[elem_index] > self.heap[parent_index]:
            # Swap parent and element if element is bigger
            self.heap[elem_index], self.heap[parent_index] = self.heap[parent_index], self.heap[elem_index]
            elem_index = parent_index
            parent_index = (elem_index - 1) // 2
            if parent_index < 0:
                return
            print("heapified up")

    def pop(self) -> Optional[int]:
        """Pop top element out of heap in O(log(n)) time"""
        if len(self.heap) == 0:
            return None

        # Pop top element and replace with last one
        element_to_return = self.heap[0]
        last_element = self.heap.pop()
        self.heap[0] = last_element

        # Calculate child node indices to bubble the value down
        cur_ind = 0
        left_child = cur_ind * 2 + 1
        if left_child >= len(self.heap):
            return
        right_child = cur_ind * 2 + 2
        if right_child >= len(self.heap):
            return

        while self.heap[cur_ind] < self.heap[left_child] or self.heap[cur_ind] < self.heap[left_child]:
            # Choose max of left and right child and swap with cur_ind
            swap_ind = max(left_child, right_child, key=lambda x: self.heap[x])
            if swap_ind == left_child:
                print("heapified left")
            else:
                print("heapified right")
            self.heap[cur_ind], self.heap[swap_ind] = self.heap[swap_ind], self.heap[cur_ind]

            # Calculate children
            cur_ind = swap_ind
            left_child = cur_ind * 2 + 1
            if left_child >= len(self.heap):
                return
            right_child = cur_ind * 2 + 2
            if right_child >= len(self.heap):
                return

        print("Popped", element_to_return)
        return element_to_return

    def pretty_print(self):
        """Prints the heap in it's tree format, every element is equal to a tab"""
        print(self.heap)
        space_string = ' '
        heap_height = int(math.log2(len(self.heap))) + 1
        cur_exp = 1
        tabs_between = 2 ** (heap_height + 1) - 1
        tabs_around = tabs_between // 2
        print(space_string * tabs_around, end='')
        for i in range(len(self.heap)):
            print(self.heap[i], end='')
            print(space_string * tabs_between, end='')
            if i >= 2 ** cur_exp - 2:
                cur_exp += 1
                tabs_between = tabs_around
                tabs_around = tabs_between // 2
                print()
                print(space_string * tabs_around, end='')
        print()

    def get_heap(self) -> list:
        return self.heap

if __name__ == "__main__":
    my_heap = Heap([1,2,3,4])
    my_heap.push(4)
    my_heap.push(1)
    my_heap.push(3)
    my_heap.push(2)
    my_heap.push(9)
    my_heap.push(7)
    my_heap.push(8)
    my_heap.pretty_print()
    my_heap.pop()
    my_heap.pop()
    my_heap.pop()
    my_heap.pop()

    my_heap.pretty_print()

