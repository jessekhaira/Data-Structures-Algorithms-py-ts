""" This module contains code for the tests for the heap
class """
import unittest
from py.data_structures.heap import Heap


class TestHeap(unittest.TestCase):
    """ This class contains unit tests for the heap data structure """

    def test_min_heap1(self):
        array = [9, 3, 1, 2, 5, 7]
        heap_obj = Heap()
        heap_obj.heapify(array)
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

    def test_min_heap2(self):
        array = [9, 3, 1, 2, 5, 7, -20, -5, -9, 12, 18, 300]
        heap_obj = Heap()
        heap_obj.heapify(array)
        # should be a min-heap - test heapify
        self.assertEqual(heap_obj.peek(array), -20)

        self.assertEqual(heap_obj.remove(array), -20)
        self.assertEqual(heap_obj.peek(array), -9)

        # Inserting -10, max priority element should be -10
        # -> testing siftUp
        heap_obj.insert(array, -100)
        self.assertEqual(heap_obj.peek(array), -100)

    def test_max_heap1(self):
        array = [9, 3, 1, 2, 5, 7]
        heap_obj = Heap(type_heap=1)
        heap_obj.heapify(array)
        self.assertEqual(array, [9, 5, 7, 2, 3, 1])

        # removing max priority element 9 - next max priority
        # should be 7 -> testing siftdown
        heap_obj.remove(array)
        self.assertEqual(heap_obj.peek(array), 7)

        # Inserting 100, max priority element should be 100
        # -> testing siftUp
        heap_obj.insert(array, 100)
        self.assertEqual(heap_obj.peek(array), 100)

    def test_max_heap2(self):
        array = [9, 3, 1, 2, 5, 7, 100, 50, -20, -90, -100, 1000, 300, 251, 12]
        heap_obj = Heap(type_heap=1)
        heap_obj.heapify(array)
        self.assertEqual(heap_obj.peek(array), 1000)

        # removing max priority element 9 - next max priority
        # should be 7 -> testing siftdown
        self.assertEqual(heap_obj.remove(array), 1000)
        self.assertEqual(heap_obj.peek(array), 300)

        # Inserting 100, max priority element should be 100
        # -> testing siftUp
        heap_obj.insert(array, 10000)
        self.assertEqual(heap_obj.peek(array), 10000)


if __name__ == "__main__":
    unittest.main()
