
class Solution(object):
    def singleNumber(self, number):
        answer = 0
        for i in number:
            answer=answer^i

        return answer
 






# For Toph compile

test = int(input())
numberlist = list(map(int, input().split()))[:test]

def single_number(number):
    answer = 0
    for i in number:
        answer ^= i 

    return answer

x = single_number(numberlist)
print(x)

