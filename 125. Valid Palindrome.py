class Solution:
    def isAlpha(self,ch)->bool:
      if (ch>='0' and ch<='9') or (ch.lower()>='a' and ch.lower()<='z') :
        return True
    def isPalindrome(self, s: str) -> bool:
      start,end=0,len(s)-1
      while(start<end):
        if not self.isAlpha(s[start]):
          start+=1
          continue
        if not self.isAlpha(s[end]):
          end-=1
          continue
        if s[start].lower()!=s[end].lower():
          return False
        start+=1
        end-=1


      return True



# Soluction 2
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i for i in s if i.isalnum()]).lower()
        return s == s[::-1]