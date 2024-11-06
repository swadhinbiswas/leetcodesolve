def find_sequence(n,s):
    dp=[0]*5
    for char in s:
        if char=="S":
            dp[4]+=dp[3]
        elif char=="P":
            dp[3]+=dp[2]
        elif char=="U":
            dp[3]+=dp[1]
        elif char=="S":
            dp[1]+=dp[0]
        elif char=="N":
            dp[0]+=dp[1]
    return dp[4]


n=int(input())
s=str(input()).strip()
result=find_sequence(n,s)
print(result)
