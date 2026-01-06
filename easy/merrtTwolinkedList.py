from typing import Optional

from typing_extensions import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        temp = head
        while list1 or list2:
            if list1 == None:
                temp.next = list2
                break
            if list2 == None:
                temp.next = list1
                break
            val1 = list1.val
            val2 = list2.val
            if val1 <= val2:
                lst = ListNode(val1)
                temp.next = lst
                temp = lst
                list1 = list1.next
            else:
                lst = ListNode(val2)
                temp.next = lst
                temp = lst
                list2 = list2.next
        return head.next


def build_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == "__main__":
    sol = Solution()

    l1 = build_list([1, 2, 4, 5, 7, 10, 11])
    l2 = build_list([1, 3, 4])

    result = sol.mergeTwoLists(l1, l2)
    print(to_list(result))
