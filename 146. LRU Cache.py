class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from collections import deque
        from collections import Counter

        self.capacity   = capacity
        self.cache      = dict()
        self.keyQueue   = deque()   # queue of keys used, left is old, right is new
        self.keyCounter = Counter() # count how many keys are in keyQueue

    def _shrinkKeyQueue(self):
        """
        When keyQueue has lots of keys appearing multiple times, we need to go over it and make it concise
        This is required, just to save space
        """
        if len(self.keyQueue) > 2 * self.capacity:
            self.keyCounter.clear()

            from collections import deque

            newKeyQueue = deque()
            while len(self.keyCounter) < len(self.cache):
                key = self.keyQueue.pop()
                if key not in self.keyCounter:
                    self.keyCounter[key] += 1
                    newKeyQueue.appendleft(key)

            self.keyQueue.clear()
            self.keyQueue = newKeyQueue

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            self.keyQueue.append(key)
            self.keyCounter[key] += 1

            self._shrinkKeyQueue() # not absolutely necessary, just to save space

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

        self._shrinkKeyQueue() # not absolutely necessary, just to save space