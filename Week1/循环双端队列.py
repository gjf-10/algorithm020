class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.front = 0
        self.rear = 0
        self.capacity = k + 1
        # 没见过这样写的
        self.arr = [0 for _ in range(self.capacity)]

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        # self.front - 1 向前挪，空出空间容纳新添加的元素，为了保证 - 1操作不会越界
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = value

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.arr[self.rear] = value
        # 维护一下指向队列尾部的指针
        self.rear = (self.rear + 1) % self.capacity


    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.capacity
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[self.rear - 1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if self.front == self.rear:
            return True

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not
        """
        return (self.rear + 1) % self.capacity == self.front