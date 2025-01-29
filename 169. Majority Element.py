# Using BruteForce 
from typing import List
from collections import defaultdict
class Solution:
    #7ms
    def majorityElement(self, nums: List[int]) -> int:
       seen={}
       for number in nums:
        if number not in seen:
           seen[number]=nums.count(number)
        
       return max(seen,key=seen.get)

    #12ms
    def majorityElement(self, nums: List[int]) -> int:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        return max(count_map, key=count_map.get)





nums=[1,1,1,2,2,3]

x=Solution().majorityElement(nums)
print(x)




