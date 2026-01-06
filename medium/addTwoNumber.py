from typing import Optional

from typing_extensions import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        temp = res

        carry = 0
        while l1 or l2:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0

            total = val1 + val2
            total = total + carry
            digit = total % 10
            lst = ListNode(digit)
            temp.next = lst
            temp = lst
            carry = total // 10
            if l1 == None and l2:
                l2 = l2.next
                continue
            if l2 == None and l1:
                l1 = l1.next
                continue
            if l1 and l2:
                l1 = l1.next
                l2 = l2.next

        if carry > 0:
            lst = ListNode(carry)
            temp.next = lst

        return res.next
