from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        tail = temp.next
        while head:
            value = head.val
            dummy = ListNode(value)
            dummy.next = tail
            tail = dummy
            head = head.next

        return tail

    def build_list(self, values):
        dummy = ListNode(0)
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next

    def to_list(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res


if __name__ == "__main__":
    sol = Solution()

    # Test 1: normal list
    head = sol.build_list([1, 2, 3, 4, 5])
    result = sol.reverseList(head)
    print(sol.to_list(result))  # expected: [5, 4, 3, 2, 1]

    # Test 2: single element
    head = sol.build_list([42])
    result = sol.reverseList(head)
    print(sol.to_list(result))  # expected: [42]

    # Test 3: empty list
    head = sol.build_list([])
    result = sol.reverseList(head)
    print(sol.to_list(result))  # expected: []
