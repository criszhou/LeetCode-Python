from collections import deque

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append( x )

    def pop(self):
        """
        :rtype: nothing
        """
        queueLen = len(self.queue)
        for i in range(queueLen-1):
            x = self.queue.popleft()
            self.queue.append(x)
        self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        queueLen = len(self.queue)
        for i in range(queueLen):
            x = self.queue.popleft()
            self.queue.append(x)
        return x

    def empty(self):
        """
        :rtype: bool
        """
        return bool(self.queue)
