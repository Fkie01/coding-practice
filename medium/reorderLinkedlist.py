from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        node = []
        while head:
            node.append(head)
            head = head.next

        i, j = 0, len(node) - 1
        while i <= j:
            node[i].next = node[j]
            i += 1
            print(i)
            print(f"j{j}")
            if i >= j:
                # node[i].next = node[i - 1]
                print("break")
                break
            node[j].next = node[i]
            j -= 1
        node[j].next = None
