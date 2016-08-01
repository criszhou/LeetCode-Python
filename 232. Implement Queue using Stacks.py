class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

        # stack1[0] is the queue front
        # stack2[0] is the queue back

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        while self.stack2:
            self.stack1.append( self.stack2.pop() )

        self.stack1.append( x )

    def pop(self):
        """
        :rtype: nothing
        """
        while self.stack1:
            self.stack2.append( self.stack1.pop() )

        self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        while self.stack1:
            self.stack2.append( self.stack1.pop() )

        return self.stack2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack1 and not self.stack2