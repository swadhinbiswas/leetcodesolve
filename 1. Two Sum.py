from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        r=len(nums)
        for i in range(r):
          frist=nums[i]
          secound=target-frist
          if secound in d:
            return [d[secound],i]
          d[nums[i]]=i

        return []

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9)) # [0, 1]
    print(s.twoSum([3, 2, 4], 6)) # [1, 2]
    print(s.twoSum([3, 3], 6)) # [0, 1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        # Return an empty list if no solution is found
        return []