// Last updated: 6/8/2026, 10:44:25 AM
1class Solution {
2    public int[] pivotArray(int[] nums, int pivot) {
3        int[] result = new int[nums.length];
4        int left = 0, right = nums.length - 1;
5        
6        for (int i = 0, j = nums.length - 1; i < nums.length; i++, j--) {
7            if (nums[i] < pivot) {
8                result[left] = nums[i];
9                left++;
10            }
11            
12            if (nums[j] > pivot) {
13                result[right] = nums[j];
14                right--;
15            }
16        }
17        
18        while (left <= right) {
19            result[left] = pivot;
20            left++;
21        }
22        
23        return result;
24    }
25}