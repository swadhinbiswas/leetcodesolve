 #problem
 #1910. Remove All Occurrences of a Substring
 # solve

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
          s=s.replace(part,"",1)
        return s

