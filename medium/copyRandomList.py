from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        dict = {}
        node = {}
        count = 0
        while head:
            dict[count] = head
            node[head] = count
            head = head.next
            count += 1

        copy = {}
        for i in dict:
            copy[i] = Node(dict[i].val)

        for i in copy:
            if dict[i].next:
                copy[i].next = copy[i + 1]
            if dict[i].random:
                j = dict[i].random
                index = node[j]
                copy[i].random = copy[index]
        dummy = Node(0)
        first = dummy
        temp = first
        for i in copy:
            temp.next = copy[i]
            temp = copy[i]

        temp.next = None
        return first.next
