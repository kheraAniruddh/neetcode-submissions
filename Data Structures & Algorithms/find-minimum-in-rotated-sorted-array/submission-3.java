class Solution {
    public int findMin(int[] nums) {
        if(nums.length==1) {
            return nums[0];
        }

        if(nums[0]<nums[nums.length-1]) {
            return nums[0];
        }
        int l=0, h=nums.length-1;
        while(l<h) {
            int mid = l + (h-l)/2;
            if (nums[mid]<nums[h]) {
                h=mid;
            } else {
                l=mid+1;
            }
        }
        return nums[l];

        
    }
}
