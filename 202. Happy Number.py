class Solution(object):
    happy_numbers = {1}
    unhappy_numbers = set()

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in Solution.happy_numbers: return True
        if n in Solution.unhappy_numbers: return False

        seen_numbers = set()
        while n not in seen_numbers and n not in Solution.happy_numbers and n not in Solution.unhappy_numbers:
            seen_numbers.add(n)
            nextN = 0
            while n > 0:
                nextN += (n % 10) ** 2
                n = n // 10
            n = nextN

        if n in seen_numbers or n in Solution.unhappy_numbers:
            Solution.unhappy_numbers |= seen_numbers
            return False
        else:
            Solution.happy_numbers |= seen_numbers
            return True
