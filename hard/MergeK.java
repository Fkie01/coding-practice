package hard;

// **Merge k Sorted Lists
// You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

// Merge all the linked-lists into one sorted linked-list and return it.

 

// Example 1:

// Input: lists = [[1,4,5],[1,3,4],[2,6]]
// Output: [1,1,2,3,4,4,5,6]
// Explanation: The linked-lists are:
// [
//   1->4->5,
//   1->3->4,
//   2->6
// ]
// merging them into one sorted linked list:
// 1->1->2->3->4->4->5->6
// Example 2:

// Input: lists = []
// Output: []
// Example 3:

// Input: lists = [[]]
// Output: []
 

// Constraints:

// k == lists.length
// 0 <= k <= 104
// 0 <= lists[i].length <= 500
// -104 <= lists[i][j] <= 104
// lists[i] is sorted in ascending order.
// The sum of lists[i].length will not exceed 104.


// * result 
// runtime 3 ms
// memory 46.2 MB

//  * Definition for singly-linked list.



class SolutionMergeK {

     public static ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0){
            return null;
        }
        int step = 1;
        while (step < lists.length) {
            for (int i = 0; i < lists.length - step; i += step * 2) {
                lists[i] = Merge(lists[i], lists[i + step]);
            }
            step *= 2;
        }
        return lists[0];
    }

    private static ListNode Merge(ListNode a, ListNode b){
        if(a == null && b == null) return null;
        ListNode dummy = new ListNode();
        ListNode head = dummy;

        while (a != null || b != null){
//            System.out.println("1");
//            System.out.println("valA" + a.val);
//            System.out.println("valB" + b.val);
            ListNode valA = (a == null) ? null : new ListNode(a.val);
            ListNode valB = (b == null) ? null : new ListNode(b.val);

            if (a == null){
                head.next = valB;
                head = head.next;
                b = b.next;
            }
            else if (b == null) {
                head.next = valA;
                head = head.next;
                a = a.next;
            } else if (a.val < b.val) {
                head.next = valA;
                head = head.next;
                a = a.next;
            }
            else {
                head.next = valB;
                head = head.next;
                b = b.next;
            }
        }
//        System.out.println(dummy);
        ListNode result = dummy.next;
        dummy.next = null;
//        System.out.println(result.val);
        return result;
    }
}

// class MergeK {
//       int val;
//       MergeK next;
//       MergeK() {}
//       MergeK(int val) { this.val = val; }
//       MergeK(int val, MergeK next) { this.val = val; this.next = next; }
// }