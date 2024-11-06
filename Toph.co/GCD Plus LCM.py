
def findelcm(number1:int, number2:int)->int:
   if number1%number2 == 0:
    return number1
   elif number2%number1 ==0:
    return number2
   else:
    return number1*number2

def findeGCD(number1: int, number2: int) -> int:
    lcm=findelcm(number1,number2)
    gcd=(number1*number2)//lcm
    return lcm+gcd

def solve(number1:int, number2:int)->str:
    if findeGCD(number1, number2)==number1+number2:
        print('true')
    else:
        print('false')


x=int(input())
for i in range(x):
    number1,number2=map(int,input().split())
    solve(number1,number2)


