class Solve:
    def tringleProblem(a:int,b:int,c:int)->None:
        try:
             x = a + b
             y = b + c
             z = a + c

             if(x >= c and y >= a and z >= b):
                print("Yes")
             else: 
                print("No")
        except Exception:
            return None




if __name__ == "__main__":
    testcase=int(input())

    for i in range(testcase):
        a, b, c = map(int, input().split())
        if a<=100 and b<=100 and c<=100:
           Solve.tringleProblem(a, b, c)
        


