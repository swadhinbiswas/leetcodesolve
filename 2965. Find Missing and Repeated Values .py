class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
      x=len(grid)
      hash_map=dict.formkeys(range(1,x*x+1),0)
      for key in hash_map:
        hash_map[key]-sum(row.count(key) for row in grid)

      return [max(hash_map,key=hash_map.get),min(hash_map,key=hash_map.get)]



#method 2
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        #math approach
        n = len(grid)
        total = n*n

        sum_val = sum(num for row in grid for num in row)
        sqr_sum = sum(num*num for row in grid for num in row)

        sum_diff = sum_val - total * (total+1) // 2
        sqr_diff = sqr_sum - total * (total+1) * (2*total+1) // 6

        repeat = (sqr_diff // sum_diff + sum_diff)//2
        missing = (sqr_diff // sum_diff - sum_diff)//2

        return [repeat, missing]
