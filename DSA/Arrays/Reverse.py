class Solve:
    def solve(array:list):
        position1,position2=0,len(array)-1
        while position1<position2:
            array[position1],array[position2]=array[position2],array[position1]
            position1+=1 
            position2-=1
        return array




array=[1,2,3,4,5,6,7,8]
print(Solve.solve(array))


