class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        LB = float("-inf")
        stack = [] # this is a stack of numbers, x in stack means we have not seen any number after x and >= x
        # numbers in stack is strickly decreasing

        for x in preorder:
            if x < LB:
                return False

            while stack and x > stack[-1]:
                LB = stack.pop() + 1

            if stack and x == stack[-1]:
                return False

            assert not stack or x < stack[-1]

            stack.append( x )

        return True