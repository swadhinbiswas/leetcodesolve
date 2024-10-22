def solve_mestrioussum(num1:int,num2:int)->int:
  sum=f"{num1+num2}{num1-num2}"
  return int(sum)


testcase=int(input())

for i in range(0,testcase):
  a,b=input().split()
  a,b=int(a),int(b)
  dic={}
  var={
    f"Case {i} : {solve_mestrioussum(a,b)}"
  }
  dic.update(var)

print(dic)

