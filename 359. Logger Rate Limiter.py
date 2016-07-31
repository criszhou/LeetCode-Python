from collections import defaultdict

class Logger(object):
    timeStoreLen = 10

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeToMessages = defaultdict(set) # maps a time to set of messages printed at that time

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        oldTimes = list( self.timeToMessages.keys() )

        # remove timestamps whare are too old
        for oldTime in oldTimes:
            if timestamp - oldTime >= self.timeStoreLen:
                del self.timeToMessages[ oldTime ]

        # printed same message recently?
        for oldTime in self.timeToMessages:
            if message in self.timeToMessages[oldTime]:
                return False

        self.timeToMessages[ timestamp ].add( message )
        return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)