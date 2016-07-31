# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, L1, L2):

        # use a dummy head to avoid differentiating initial setup and following process
        dummyHead = ListNode(None)
        tail = dummyHead

        addOne = 0
        while L1 or L2 or addOne:
            newVal = (L1.val if L1 else 0) + (L2.val if L2 else 0) + addOne
            addOne, newVal = divmod(newVal, 10)

            tail.next = ListNode(newVal)
            tail = tail.next

            if L1: L1 = L1.next
            if L2: L2 = L2.next

        return dummyHead.next