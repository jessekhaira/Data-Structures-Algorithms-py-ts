import unittest
from py.data_structures.heap import Heap


class tests(unittest.TestCase):

    def testMinHeap(self):
        array = [9, 3, 1, 2, 5, 7]
        heap_obj = Heap()
        heap_obj.heapify(array)
        print(array)
        # should be a min-heap - test heapify
        self.assertEqual(array, [1, 2, 7, 3, 5, 9])

        # removing max priority element 1 - next max priority
        # should be 2 -> testing siftdown
        heap_obj.remove(array)
        self.assertEqual(heap_obj.peek(array), 2)

        # Inserting -10, max priority element should be -10
        # -> testing siftUp
        heap_obj.insert(array, -10)
        self.assertEqual(heap_obj.peek(array), -10)

    def testMaxHeap(self):
        array = [9, 3, 1, 2, 5, 7]
        heap_obj = Heap(type_heap=1)
        heap_obj.heapify(array)
        print(array)
        self.assertEqual(array, [9, 5, 7, 2, 3, 1])

        # removing max priority element 9 - next max priority
        # should be 7 -> testing siftdown
        heap_obj.remove(array)
        self.assertEqual(heap_obj.peek(array), 7)

        # Inserting 100, max priority element should be 100
        # -> testing siftUp
        heap_obj.insert(array, 100)
        self.assertEqual(heap_obj.peek(array), 100)


if __name__ == "__main__":
    unittest.main()
