package medium;
//  ** Swap Nodes in Pairs
// Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

// Example 1:

// Input: head = [1,2,3,4]

// Output: [2,1,4,3]

// Example 2:

// Input: head = []

// Output: []

// Example 3:

// Input: head = [1]

// Output: [1]

// Example 4:

// Input: head = [1,2,3]

// Output: [2,1,3]

 

// Constraints:

// The number of nodes in the list is in the range [0, 100].
// 0 <= Node.val <= 100
// *result
// runtime 5 ms
// memory 41.2 MB

class SolutionSwapPair {
    public static ListNode swapPairs(ListNode head) {

        ListNode dummy = new ListNode(0,head);
        ListNode pre = dummy, cur = head;
//        if (dummy == null) return null;
        System.out.println(pre.val);
        while (cur != null && cur.next != null){
            // System.out.println(cur.next.val);
            ListNode lt1 = cur.next;
            ListNode lt2 = cur.next.next;


            lt1.next = cur;
            cur.next = lt2;
            pre.next = lt1;


            pre = cur;
            cur = lt2;
        }
        return dummy.next;
    }
}

