
class Solution(object):
    def singleNumber(self, number):
        answer = 0
        for i in number:
            answer=answer^i

        return answer
 


