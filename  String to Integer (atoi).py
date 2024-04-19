class Solution:
    def myAtoi(self, s: str) -> int:
       num:int = 0
       
       for i in range(len(s)):
          sign:int = 1
          if s[i]=='-':
            sign = -1
          elif s[i]==' ':
            continue
          elif s[i].isdigit():
            num = num * 10 + int(s[i])
            if num > 2**31-1:
              return 2**31-1
            if num < -2**31:
              return -2**31
          else:
            break
          
          return num * sign
        
        
        

# Time Complexity: O(n)


c=Solution()
print(c.myAtoi("4245 fuck you")) #42