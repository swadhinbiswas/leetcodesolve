class Solve:
    def convertToBinary(number:int):
        ans:float=0
        power:int=1
    
        while number>0:
            rem=number%2   
            number//=2
            ans+=(rem*power)
            power*=10

        return ans




if __name__ == "__main__":
    number=50
    x=Solve.convertToBinary(number=number)
    print(x)
