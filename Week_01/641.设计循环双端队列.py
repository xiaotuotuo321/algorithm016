"""
641.设计循环双端队列
"""


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.queue = [0] * k
        self.head, self.count = 0, 0  # with head and count means that we don't need tail pointer
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        self.queue[(self.head - 1) % self.capacity] = value
        self.head = (self.head - 1) % self.capacity
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        self.queue[(self.head + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.count -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.count == 0:
            return -1
        return self.queue[self.head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.count == 0:
            return -1
        return self.queue[(self.head + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.count == self.capacity
