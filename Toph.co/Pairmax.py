class Solve:
    def __init__(self,list1)->int:
        self.list1 = list1
        self.list2 = []
        self.list3 = []
        self.list4 = []
        self.maxvalue=0

    def solveing(self):
        for i in self.list1:
            if i%2 == 0:
                self.list2.append(i)
            else:
                self.list3.append(i)
        if len(self.list3) == 0:
            return -1
        else:
            for i in self.list3:
                for j in self.list2:
                    self.list4.append(i*j)

        self.maxvalue=max(self.list4)

        return self.maxvalue


    
    

if __name__ == '__main__':
    x=int(input())
    list1=[int(x) for x in input().split()][:x]
    x=Solve(list1)
    z=x.solveing()
    print(z)


