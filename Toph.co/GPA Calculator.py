def solve(x,n):
    result=sum(x)/n
    return result



if __name__=="__main__":
    testcase=int(input())
    for i in range(testcase):
        n=int(input())
        x=[]
        for i in range(n):
            x.append(input())
        result=solve(x,n)
        print(f"Case {i}: {result:.3f} ")
