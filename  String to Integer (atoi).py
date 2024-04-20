class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
       
        out=0
        if not s:
            return 0
        negative=False
        if s[0] == '-':
            negative=True
        elif s[0] == '+':
            negative=False
        elif not s[0].isnumeric():
            return 0
        else:
            out=ord(s[0])-ord("0")

        for i in range(1,len(s)):
            if s[i].isnumeric():
                out=out*10+(ord(s[i])-ord("0"))
            else:
                break

        
      
        if not negative and out>=2147483647:
            return 2147483648

        if out>=2147483648 and negative:
            return -2147483648


        if not negative:
            return out
        else:
            return -out


        # if not s:
        #     return 0
        
        # negatives = False
        # out=0
        # if s[0]=='-':
        #     negatives = True
        # elif s[0]=='+':
        #     negatives = True
        # elif not s[0].isnumeric():
        #     return 0
        # else:
        #     out = ord(s[0])-ord("0")
        # for i in range(1,len(s)):
        #     if s[i].isnumeric():
        #         out=out*10+(ord(s[i])-ord("0"))
        #     if not negatives and out >= 2**31:
        #         return 2**31
        #     if negatives and out<=-2**31:
        #         return -2**31
        #     else:
        #         break
        
        # if not negatives:
        #     return out
        # else:
        #     return -out 

            

b=Solution()

x=b.myAtoi(s="3.14159")
print(x)

        