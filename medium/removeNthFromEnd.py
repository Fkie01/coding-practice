from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = []
        while head:
            node.append(head)
            head = head.next
        size = len(node)
        delete_node = size - n
        print(delete_node)
        count = 0
        dummy = ListNode()
        first = dummy
        temp = first
        while count <= size - 1:
            print(count)
            if count == delete_node:
                print("break")
                node[count - 1].next = None
                count += 1
                continue
            print("check")
            temp.next = node[count]
            temp = node[count]
            count += 1

        return first.next
