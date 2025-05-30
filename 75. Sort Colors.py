class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mid=0;start=0;end=len(nums)-1
        while(mid<=end):
            if nums[mid]==0:
                nums[start],nums[mid]=nums[mid],nums[start]
                mid+=1;start+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[end],nums[mid]=nums[mid],nums[end]
                end-=1


# Run time 0 ms