class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      if needle == '':
        return -1
      else:
        return haystack.find(needle)



haystack = "hello"
needle = "ll"
solution = Solution()
print(solution.strStr(haystack, needle)) # 2