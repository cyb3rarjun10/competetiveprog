// Last updated: 3/18/2026, 8:50:26 AM
1int search(int* nums, int numsSize, int target) {
2    int l=0;
3    int r=numsSize;
4    while (l<r){
5        int mid = (l+r)/2;
6        if(nums[mid]==target){
7            return mid;
8        }
9        else if(nums[mid]>target){
10            r=mid;
11        }
12        else{
13            l=mid+1;
14        }
15    }
16    return -1;
17}