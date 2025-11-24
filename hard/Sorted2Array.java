package hard;

//**Median of Two Sorted Arrays */
// Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

// The overall run time complexity should be O(log (m+n)).

 

// Example 1:

// Input: nums1 = [1,3], nums2 = [2]
// Output: 2.00000
// Explanation: merged array = [1,2,3] and median is 2.
// Example 2:

// Input: nums1 = [1,2], nums2 = [3,4]
// Output: 2.50000
// Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

// Constraints:

// nums1.length == m
// nums2.length == n
// 0 <= m <= 1000
// 0 <= n <= 1000
// 1 <= m + n <= 2000
// -106 <= nums1[i], nums2[i] <= 106

// * result
// runtime 2 ms
// memory 46 MB

class SolutionSorted2Array {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] result = mergeInto(nums1, nums2);
        int size = result.length / 2;
        double ans = 0;
        if(result.length % 2 != 0){
            ans = result[size];
        }
        else {
            int sum = result[size] + result[size-1];
            ans = (double) sum / 2;
        }
        return ans;
    }

    public static int[] mergeInto(int[] num1, int[] num2){
        int total = num1.length + num2.length;
        int[] result = new int[total];
        int i = 0, j = 0;
        for(int u = 0; u < total; u++){
            if (i >= num1.length){
                result[u] = num2[j++];
            }
            else if(j >= num2.length){
                result[u] = num1[i++];
            }
            else if (num1[i] <= num2[j]) {
                result[u] = num1[i++];
            }
            else {
                result[u] = num2[j++];
            }
        }
        return result;
    }
}