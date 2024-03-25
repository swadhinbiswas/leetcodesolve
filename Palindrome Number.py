class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        while x > 0:
            if x % 10 != x // 10 ** (len(str(x)) - 1):
                return False
            x = (x % 10 ** (len(str(x)) - 1)) // 10
        return True



if __name__ == "__main__":
  #testcase1
  s = Solution()
  a=s.isPalindrome(121)
  b=s.isPalindrome(-121)
  c=s.isPalindrome(10)
  d=s.isPalindrome(1000021)
  print(a) #True
  print(b) #False
  print(c) #False
  print(d) #False
 