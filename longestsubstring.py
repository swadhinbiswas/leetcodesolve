class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = answer = 0
        chars = [-1]*128
        for r, ch in enumerate(s):
            if chars[ord(ch)] >= l:
                l = chars[ord(ch)]+1
            else:
                answer = max(answer, r-l+1)
            chars[ord(ch)] = r
        return answer
      
      
solve=Solution()
print(solve.lengthOfLongestSubstring("abcabcbb"))
print(solve.lengthOfLongestSubstring("bbbbb"))
print(solve.lengthOfLongestSubstring("pwwkew"))
print(solve.lengthOfLongestSubstring(""))
print(solve.lengthOfLongestSubstring(" "))