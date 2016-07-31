class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from collections import deque
        from collections import Counter

        self.capacity = capacity
        self.cache = dict()
        self.keyQueue = deque() # queue of keys used
        self.keyCounter = Counter() # count how many keys are in keyQueue

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            self.keyQueue.append(key)
            self.keyCounter[key] += 1
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        self.cache[key] = value
        self.keyQueue.append(key)
        self.keyCounter[key] += 1

        while len(self.cache) > self.capacity:
            oldestKey = self.keyQueue.popleft()
            self.keyCounter[oldestKey] -= 1
            if self.keyCounter[oldestKey]==0:
                del self.keyCounter[oldestKey]
                del self.cache[oldestKey]