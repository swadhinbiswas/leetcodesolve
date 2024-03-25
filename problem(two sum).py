from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i
        return []
      
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9)) # [0, 1]
    print(s.twoSum([3, 2, 4], 6)) # [1, 2]
    print(s.twoSum([3, 3], 6)) # [0, 1]